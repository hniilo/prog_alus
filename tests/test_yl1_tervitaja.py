import json
import sys
import unittest
from pathlib import Path


PROJEKTI_JUUR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJEKTI_JUUR))

from w3_praktikum.yl1_tervitaja import kysi_synniaasta


TESTANDMETE_TEE = Path(__file__).parent / "testdata" / "synniaasta_juhtumid.json"
PRAEGUNE_AASTA = 2026


class SynniaastaKusimiseTestid(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with TESTANDMETE_TEE.open(encoding="utf-8") as fail:
            cls.juhtumid = json.load(fail)

    def test_synniaasta_juhtumid(self):
        for juhtum in self.juhtumid:
            with self.subTest(juhtum=juhtum["nimi"]):
                sisendid = iter(juhtum["sisendid"])
                teated = []

                tulemus = kysi_synniaasta(
                    sisend=lambda _kusimus: next(sisendid),
                    valjund=teated.append,
                    praegune_aasta=PRAEGUNE_AASTA,
                )

                self.assertEqual(juhtum["oodatud_synniaasta"], tulemus)
                self.assertEqual(juhtum["oodatud_teated"], teated)


if __name__ == "__main__":
    unittest.main()
