import json
import sys
import unittest
from pathlib import Path


PROJEKTI_JUUR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJEKTI_JUUR))

from w3_praktikum.yl1_tervitaja import kysi_synniaasta


TESTANDMETE_TEE = Path(__file__).parent / "testdata" / "synniaasta_juhtumid.json"
PRAEGUNE_AASTA = 2026

with TESTANDMETE_TEE.open(encoding="utf-8") as fail:
    JUHTUMID = json.load(fail)


class SynniaastaKusimiseTestid(unittest.TestCase):
    pass


def loo_test(juhtum):
    """Loob ühe testandmete kirjega seotud unittesti testi."""
    def test(self):
        sisendid = juhtum["sisendid"]
        iter_sisendid = iter(sisendid)
        teated = []

        tulemus = kysi_synniaasta(
            sisend=lambda _kusimus: next(iter_sisendid),
            valjund=teated.append,
            praegune_aasta=PRAEGUNE_AASTA,
        )

        print(f"\nTest: {juhtum['nimi']}")
        print(f"  Sisendid: {sisendid}")
        print(f"  Oodatud sünniaasta: {juhtum['oodatud_synniaasta']}")
        print(f"  Tegelik sünniaasta: {tulemus}")
        print(f"  Oodatud teated: {juhtum['oodatud_teated']}")
        print(f"  Tegelikud teated: {teated}")

        self.assertEqual(juhtum["oodatud_synniaasta"], tulemus)
        self.assertEqual(juhtum["oodatud_teated"], teated)

    return test


for number, juhtum in enumerate(JUHTUMID, start=1):
    testi_nimi = f"test_{number:02d}"
    setattr(SynniaastaKusimiseTestid, testi_nimi, loo_test(juhtum))


if __name__ == "__main__":
    unittest.main()
