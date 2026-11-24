import math

import pytest
from pydantic import ValidationError

from edb.api.routes.kv import KVSetRequest


def test_ttl_defaults_to_none():
    assert KVSetRequest(value=1).ttl is None


@pytest.mark.parametrize("ttl", [1, 1.5, 0.001, 3600])
def test_positive_ttl_is_accepted(ttl):
    assert KVSetRequest(value=1, ttl=ttl).ttl == ttl


@pytest.mark.parametrize("ttl", [0, -1, -0.5, math.inf, -math.inf, math.nan])
def test_zero_negative_or_non_finite_ttl_is_rejected(ttl):
    with pytest.raises(ValidationError):
        KVSetRequest(value=1, ttl=ttl)
