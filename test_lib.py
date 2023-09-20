"""
Test for library goes here

"""
import lib
import pandas as pd


def test_pd_mean():
    df = pd.read_csv("bmi.csv")
    result = lib.pd_mean(df["Age"])
    assert result == 31.61808367071525


def test_pd_median():
    df = pd.read_csv("bmi.csv")
    result = lib.pd_median(df["Weight"])
    assert result == 72.9


def test_pd_std():
    df = pd.read_csv("bmi.csv")
    result = round(lib.pd_std(df["Height"]), 6)
    assert result == 0.085974


if __name__ == "__main__":
    test_pd_mean()
    test_pd_median()
    test_pd_std()
