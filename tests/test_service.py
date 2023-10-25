from datetime import datetime, timedelta

import pytest

from todate.service import get_time


def test_getting_time():
    result = get_time("yesterday").date()
    expected_result = (datetime.now() - timedelta(days=1)).date()
    assert result == expected_result


def test_invalid_prompt():
    with pytest.raises(ValueError):
        get_time("foobar")
