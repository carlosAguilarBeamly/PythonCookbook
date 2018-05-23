# -*- coding: utf-8 -*-
"""Pandas date and time operations

This module contains quick recipes to operate with time, dates and timestamps
in Pandas.

Example:
        $ python recipe_extract_timestamp_values.py

Todo:
    * Include more examples
    * You have to also use ``sphinx.ext.todo`` extension

"""

import pandas as pd
import datetime as dt


def recipe_extract_timestamp_values():
    """Extract features from timestamp columns

    The following recipe shows how to extract meaningful
    values from a timestamp.

    Examples:
        Create a Pandas Series object with one timestamp and extract the month::

            $ df = pd.DataFrame([{'Timestamp': pd.tslib.Timestamp.now()}]);
            $ df['month']       = df.Timestamp.dt.month;
            $ df['hour']        = df.Timestamp.dt.hour;
            $ df['day']         = df.Timestamp.dt.day;
            $ df['day_of_week'] = df.Timestamp.dt.dayofweek;

    Category: Pandas
    Topic: Time and date

    """

    df = pd.DataFrame([{'Timestamp': pd.tslib.Timestamp.now()}]);

    df['month']       = df.Timestamp.dt.month;
    df['hour']        = df.Timestamp.dt.hour;
    df['day']         = df.Timestamp.dt.day;
    df['day_of_week'] = df.Timestamp.dt.dayofweek;



def recipe_filter_df_by_timestamp_values(df, minDate, maxDate):
    """Filter a timestamp columns

    This recipe shows how to filter a DF by timestamp dates returning both the
    filtered DF and the indexes.

    Examples::

            $ minTimeStamp = dt.datetime(2017, 5, 1, 14, 00);
            $ maxTimeStamp = dt.datetime(2017, 12, 1, 17, 00);
            $ dates = [pd.Timestamp('2017-04-21'), pd.Timestamp('2017-07-01'), pd.Timestamp('2018-01-03')]
            $ ts = pd.Series(np.random.randn(3), dates)
            $ df = pd.Series(np.random.randn(3), dates)
            $ a,b = recipe_filter_df_by_timestamp_values(df, minDate, maxDate);

    Args:
        df (DF): A dataframe with a column named 'Timestamp'.
        minDate (datetime): The minimum date.
        maxDate (datetime): The maximum date.

    Returns:
        df_filtered: The filtered DF.
        idx_valid_dates: The indexes of the valid dates.

    Category: Pandas
    Topic: Time and date

    """
    minTimeStamp = dt.datetime(2017, 5, 1, 14, 00);
    maxTimeStamp = dt.datetime(2017, 12, 1, 17, 00);

    idx_valid_dates = (df['Timestamp'] > minTimeStamp) & (df['Timestamp'] < maxTimeStamp);
    df_filtered     = df[idx_valid_dates];

    return df_filtered, idx_valid_dates;