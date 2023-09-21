"""
Test for library goes here

"""
from lib import pd_read, pd_mean, pd_median, pd_std
import pandas as pd


def test_pd_read():
    file_path = "bmi.csv"
    data_csv = pd_read(file_path)
    assert isinstance(data_csv, pd.DataFrame)
    assert not data_csv.empty


def test_pd_mean():
    df = pd.read_csv("bmi.csv")
    result = pd_mean(df["Age"])
    assert result == 31.61808367071525


def test_pd_median():
    df = pd.read_csv("bmi.csv")
    result = pd_median(df["Weight"])
    assert result == 72.9


def test_pd_std():
    df = pd.read_csv("bmi.csv")
    result = round(pd_std(df["Height"]), 6)
    assert result == 0.085974


if __name__ == "__main__":
    test_pd_read()
    test_pd_mean()
    test_pd_median()
    test_pd_std()
