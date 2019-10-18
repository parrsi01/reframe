import pytest
import pandas as pd
from reframe import Relation

country = Relation("country.csv")

def test_antijoin():
    expected = Relation("tests/antijoin.csv", sep="|").reset_index().drop(columns=["index"])
    observed = country.query('continent == "North America"').project(['name','region']).antijoin(country.query('region == "Caribbean"').project(['name', 'region'])).reset_index().drop(columns=["index"])
    assert observed.equals(expected)