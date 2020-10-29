import pytest
from src.date_extraction import extract_date_from_str
from src.date_extraction import patterns_list
import datetime as dt

test_cases = [
    ('*2011/12/01 08:15:27.123456_blabla.xlsx', dt.datetime(year=2011, month=12, day=1, hour=8, minute=15, second=27, microsecond=123456)),
    ('*2011-12-01 08:15:27.123456_blabla.xlsx', dt.datetime(year=2011, month=12, day=1, hour=8, minute=15, second=27, microsecond=123456)),
    ('*2011.12.01 08:15:27.123456_blabla.xlsx', dt.datetime(year=2011, month=12, day=1, hour=8, minute=15, second=27, microsecond=123456)),
    ('*2011 12 01 08:15:27.123456_blabla.xlsx', dt.datetime(year=2011, month=12, day=1, hour=8, minute=15, second=27, microsecond=123456)),
    ('*20111201 08:15:27.123456_blabla.xlsx', dt.datetime(year=2011, month=12, day=1, hour=8, minute=15, second=27, microsecond=123456)),
    ('*10-12-2011 08:15:27.123456_blabla.xlsx', dt.datetime(year=2011, month=10, day=12, hour=8, minute=15, second=27, microsecond=123456)),
    ('*10-12-2011_bla.txt', dt.datetime(year=2011, month=10, day=12)),
    ('*2011-12-31_bla.txt', dt.datetime(year=2011, month=12, day=31)),
    ('*20111231_bla.txt', dt.datetime(year=2011, month=12, day=31))
    ]

@pytest.mark.parametrize("test_input, expected", test_cases)
def test_date_from_string(test_input, expected):
    assert extract_date_from_str(patterns_list=patterns_list, string=test_input) == expected