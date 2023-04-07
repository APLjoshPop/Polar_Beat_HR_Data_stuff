# imports
import pandas as pd
import json

import plotly.express as px

# open and read the polar json file into a pandas data frame using a context manager
with open(
    "training-session-2023-01-30-7571231964-40ac83fa-28c0-4512-ab35-fa0a2aa206fc.json",
) as polar_json_file:
    polar_json_data = json.load(polar_json_file)

exercises = polar_json_data["exercises"]
# Error checking the data in the jason file
if len(exercises) != 1:
    raise ValueError("There should only be one exercise in the json file.")

# get the first and only exercise
exercise = exercises[0]

# NOTE: exercises is a list of dictionaires, a dictionary for each exercise, each exercise has various characteristics,
# ...one of which i the samples dictionary with hearRate which is a list

# NOTE: polar_json_data["exercises"][0]["samples"]["heartRate"] --> the list of dateTime and Value, construct must be passed in a way that
# ...pandas knows how to create the datafraem your looking for.

# QUESTION: why didn't the code line below work at renaming the columns? it produced NaN data...
# ...was trying method 1 here: https://www.geeksforgeeks.org/different-ways-to-create-pandas-dataframe/
# df = pd.DataFrame(exercise["samples"]["heartRate"], columns=["date_time", "heart_rate"])
# ANSWER: You're saying these are the columns I want from the data set, and since they don't exist in the df they are just empty.

df = pd.DataFrame(exercise["samples"]["heartRate"])

# renaming the column names
df.rename(
    columns={"dateTime": "date_time", "value": "heart_rate"},
    inplace=True,
)

# add a column that shows the difference between the current rows heart rate value and the last rows heart rate value
df["change_in_heart_rate"] = df["heart_rate"].diff()

# add a column that shows the difference in time between heart beats
df["date_time"] = pd.to_datetime(df["date_time"])
df["change_in_time_between_heart_beats"] = df["date_time"].diff()


# px.line(df, x="date_time", y="heart_rate")

print(df)
# print(pd.unique(df["change_in_time_between_heart_beats"]))
# print(pd.unique(df["change_in_heart_rate"]))
# print(df.loc[df["change_in_heart_rate"] > 0.0])
#
# 2023.04.07: go ahead and create a method that just returns a dataframe, and then import that method into your jupiter notebook.
# and then do graphing and analysis in jbook
# What are the descrete things you need to do that can be broken out into different methods and different python files?
# --> it's subjective but: single responsibility principle, each piece of code (function) should do one thing and do it well.
# ------>Functions are units of reuse (call more than one time) or a means of organizing code to make it easier to understand.
# -------> you want to break your code down into easily digestible pieces that are clearly named.
# ------> Classes and modules use the same principle as functions, want to be able to reason about all the code you see on screen.
# one function for ingesting data, and one function for performing the HR variability calculations and that to the df.
# May initially use jbook to prototype your code before turning it into a module. jupyter is probably better than jbook to refer to jupyter Notebook files.
# on flake 8 issues try to fix those as they come up. don't make a mess and come back to clean it up. clean it up as you go.
# Also fix all problems in problem tab below. (flake 8 issues)
