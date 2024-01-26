import pytest
import bday_estimator


def test_days_used():
    assert bday_estimator.days_used() == 26
