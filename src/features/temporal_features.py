"""Temporal aggregate helpers."""
import pandas as pd

def add_time_of_day(df):
    df["time_of_day"] = pd.cut(
        df["hour"], bins=[-1, 6, 12, 18, 24],
        labels=["night", "morning", "afternoon", "evening"]
    )
    return df

def hourly_aggregate(df, value_cols, platform_label):
    agg = df.groupby("hour_bin")[value_cols].mean().reset_index()
    agg["platform"] = platform_label
    return agg