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


def scatterplot(data):
    plt.scatter(data["Age"], data["Bmi"], alpha=0.5)
    plt.xlabel("Age")
    plt.ylabel("BMI")
    plt.title("Scatter Plot of Age vs BMI")
    plt.grid(True)
    plt.savefig("agebmi_scatterplot.png")
    plt.show()
    plt.close()
