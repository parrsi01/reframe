import pytest
import pandas as pd
from reframe import Relation

country = Relation('country.csv')

@pytest.fixture
def r():
    r = Relation('country.csv')
    return r

def test_antijoin(r):
    r = country.query('continent == "North America"').project(['name','region']).antijoin(country.query('region == "Caribbean"').project(['name', 'region'])).reset_index().drop(columns=["index"])
    data_expected = Relation("tests/antijoin.csv", sep="|").reset_index().drop(columns=["index"])
    df_expected = pd.DataFrame(data=data_expected)
    r_expected = Relation(df_expected)
    assert r.equals(r_expected)