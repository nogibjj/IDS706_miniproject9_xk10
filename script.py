"""
Main cli or app entry point
"""
from lib import pd_desc
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def summary_desc():
    df = pd.read_csv("bmi.csv")
    return pd_desc(df)

def histogram(data):
    plt.figure(figsize=(8, 6))
    sns.histplot(data["Age"], kde=True, color="skyblue")
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.savefig("age_histogram.png")
    plt.show()
    plt.close()
