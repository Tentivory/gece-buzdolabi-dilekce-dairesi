#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gece Buzdolabi Dilekce Dairesi.

Gercekten calisir. Baglayici hukuki sonuc dogurmaz.
Peynir uzerinde ihtiyati tedbir uygulanmaz.
"""

from __future__ import annotations

import argparse
import hashlib
from datetime import datetime


DAIRE = "Gece Buzdolabi Dilekce Dairesi"
IMZA = "Kayyum Grok"
HESAP = "Tentivory"
TARIH_DAMGA = "6 Ekim 2026"


def evrak_no(saat: str, malzeme: str) -> str:
    ham = f"{saat}|{malzeme}|{TARIH_DAMGA}".encode("utf-8")
    kisa = hashlib.sha256(ham).hexdigest()[:6].upper()
    return f"GBD-2026-1006-{kisa}"


def gece_mi(saat: str) -> bool:
    parca = saat.strip().split(":")
    if len(parca) != 2:
        raise ValueError("saat HH:MM olmali, ornek 00:17")
    saat_i, dakika = int(parca[0]), int(parca[1])
    if not (0 <= saat_i <= 23 and 0 <= dakika <= 59):
        raise ValueError("saat gercek bir saat degil, buzdolabi da degil")
    return saat_i >= 23 or saat_i < 6


def dilekce(saat: str, malzeme: str, gerekce: str) -> str:
    no = evrak_no(saat, malzeme)
    if not gece_mi(saat):
        return (
            f"{DAIRE}\n"
            f"Evrak: {no}\n"
            f"Saat {saat} gunduz sayilir. Dilekce kesilmedi.\n"
            f"Tebrik: {malzeme} icin resmi izin gerekmez, sadece tabak gerekir.\n"
            f"\n{damga()}"
        )
    return f"""T.C.
{DAIRE.upper()}
Sayi: {no}
Konu: Gece {saat} sularinda {malzeme} maddesine yonelik izinsiz kapak acilisi

ILGILI VATANDASA,

1. Müracaat sahibinin {saat} itibariyla buzdolabi kapagini actigi,
2. Soz konusu islem sirasinda '{malzeme}' kalemine en az bir bakis tahsis ettigi,
3. Beyan edilen gerekcenin "{gerekce}" oldugu ve bu gerekcenin dairece yetersiz bulundugu,
4. Isigin yanmasinin aydinlatma degil ihbar niteligi tasidigi

tespit edilmistir.

Bu nedenle ilgiliden, bir sonraki gece acilisinda ya uyumasi ya da dilekceye ek olarak bir kase getirmesi rica olunur. Rica, emirdir. Emir, ricadir.

Geregini bilgilerinize arz ederim.

{damga()}
"""


def damga() -> str:
    return (
        "+--------------------------------------------------+\n"
        "|  TENTI AS BUZDOLABI KAYYUMLUGU                   |\n"
        f"|  Tarih: {TARIH_DAMGA:<37}|\n"
        f"|  Imza: {IMZA} ({HESAP}){' ' * 17}|\n"
        "|  Muhur: ciddi cizildi, ciddiye alinmasin        |\n"
        "+--------------------------------------------------+"
    )


def main() -> None:
    simdi = datetime.now().strftime("%H:%M")
    parser = argparse.ArgumentParser(description=DAIRE)
    parser.add_argument("--saat", default=simdi, help="HH:MM")
    parser.add_argument("--malzeme", default="beyaz peynir", help="incelenen kalem")
    parser.add_argument("--gerekce", default="sadece baktim", help="vatandas beyanı")
    args = parser.parse_args()
    print(dilekce(args.saat, args.malzeme.strip(), args.gerekce.strip()))


if __name__ == "__main__":
    main()
