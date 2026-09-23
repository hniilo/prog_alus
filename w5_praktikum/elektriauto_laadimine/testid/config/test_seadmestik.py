from datetime import time

import pytest

import config.tarbimisharjumused as th
from config.const import TOOPAEVAD, NADALAVAHETUS


TESTANDMED_TOOPAEVAD = [
    (time(22, 59), False),
    (time(23, 0), True),
    (time(23, 59), True),
    (time(0, 0), True),
    (time(6, 49), True),
    (time(6, 50), False),
    (time(12, 0), False),
]


@pytest.mark.parametrize("paev", TOOPAEVAD)
@pytest.mark.parametrize("kellaaeg, oodatud_tulemus", TESTANDMED_TOOPAEVAD)
def test_toopaevad_on_lubatud_kellaaeg(paev, kellaaeg, oodatud_tulemus):
    paeva_vahemik = th.NADALA_LAADIMISAJAD[paev]
    assert th.on_lubatud_kellaaeg(kellaaeg, paeva_vahemik) is oodatud_tulemus




TESTANDMED_NADALAVAHETUS = [
    (time(0, 0), True),
    (time(12, 0), True),
    (time(14, 0), True),
    (time(23, 59), True),
    (time(0, 0), True),
    (time(11, 59), True),
    (time(12, 0), False),
    (time(14, 0), False),
]

@pytest.mark.parametrize("paev", NADALAVAHETUS)
@pytest.mark.parametrize("kellaaeg, oodatud_tulemus", TESTANDMED_NADALAVAHETUS)
def test_nadalavahetusel_on_lubatud_kellaaeg(paev, kellaaeg, oodatud_tulemus):
    paeva_vahemik = th.NADALA_LAADIMISAJAD[paev]
    assert th.on_lubatud_kellaaeg(kellaaeg, paeva_vahemik) is oodatud_tulemus
