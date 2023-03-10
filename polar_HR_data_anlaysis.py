# imports
import pandas as pd
import json

# open and read the polar json file into a pandas data frame
polar_json_file = open(
    "training-session-2023-01-30-7571231964-40ac83fa-28c0-4512-ab35-fa0a2aa206fc.json"
)

polar_json_data = json.load(polar_json_file)
exercises = polar_json_data["exercises"]

# Error checking the data in the jason file
if len(exercises) != 1:
    raise ValueError("There should only be one exercise in the json file.")

# grap the first and only exercise
exercise = exercises[0]

# exercises is a list of dictionaires, a dictionary for each exercise, each exercise has various characteristics, one of which i the samples dictionary with hearRate which is a list
# polar_json_data["exercises"][0]["samples"]["heartRate"] --> the list of dateTime and Value, construct must be passed in a way that pandas knows how to create the datafraem your looking for
df = pd.DataFrame(exercise["samples"]["heartRate"])
print(df)
polar_json_file.close()

# polar_json_df = pd.read_json('training-session-2023-01-30-7571231964-40ac83fa-28c0-4512-ab35-fa0a2aa206fc.json')
# homework look up file io using a context manager in python for 3/10/2023 homework.
# now that I have the dataframe rename the columns to be more descriptive date_time --> date_time, value --> heartrate
