import pandas as pd
import pytest
from reframe import Relation

@pytest.fixture
def r():
    r = Relation('country.csv')
    return r


def test_count(r):
    r = r.groupby(['continent']).count("capital")
    data_expected = {"continent" : ["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"], "count_capital" : [57,0,51,46,37,27,14]}
    df_expected = pd.DataFrame(data=data_expected)
    r_expected = Relation(df_expected)
    assert r.equals(r_expected)

def test_count2(r):
    r = r.groupby(['continent']).count("name")
    data_expected = {"continent" : ["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"], "count_name" : [58,5,51,46,37,28,14]}
    df_expected = pd.DataFrame(data=data_expected)
    r_expected = Relation(df_expected)
    assert r.equals(r_expected)
