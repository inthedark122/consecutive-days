from typing import List

import pandas as pd
import numpy as np

from .exceptions import EmptyException

class ConsecutiveDays():
  def __init__(self, dates: List[str]):
    """Initialize ConsecutiveDays
    Load dates into DataFrame

    Args:
        dates (list[str]): List of the dates. Example: ["2023-03-24 05:02:54", "2023-03-23 08:02:54"]
    """
    self.load(dates)

  def load(self, dates: List[str]):
    """
    Load dates and convert them to the next processes
    """
    self.df = pd.DataFrame({"date": dates})
    self.df["date"] = pd.to_datetime(self.df["date"], errors="coerce")
    self.df.dropna(inplace=True)

    if self.df.empty:
      raise EmptyException()

    self.df["date_only"] = self.df["date"].dt.date
    self.df.sort_values(by=["date_only"], inplace=True)
    self.df["grp_date"] = self.df["date_only"].diff().dt.days.gt(1).cumsum()

  def process(self) -> pd.DataFrame:
    """
    Make consecutive DataFrame of days
    """
    df_days = self.df.groupby("grp_date").agg(
      START=pd.NamedAgg("date_only", "first"),
      END=pd.NamedAgg("date_only", "last"),
      LENGTH=pd.NamedAgg("date_only", lambda x: ((x.iloc[-1] - x.iloc[0]).days + 1))
    )
    df_days.sort_values(by=["LENGTH"], inplace=True, ascending=False)
    return df_days

  def print(self, df):
    print(df.to_markdown(index=False))
