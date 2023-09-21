import pandas as pd

# read the Dataframe bmi.csv
def pd_read(data):
    df = pd.read_csv(data)
    return df


# generate summary statistics
def pd_desc(df):
    return df.describe()


# generate mean
def pd_mean(df):
    return df.mean()


# generate median
def pd_median(df):
    return df.median()


# generate standard error
def pd_std(df):
    return df.std()
