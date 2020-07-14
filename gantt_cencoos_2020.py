# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 16:25:34 2020

@author: JiM taken directly from web example
requires a "task.csv" file with various tasks
requires, in my case, to issue "conda install altair" from the anaconda3/condabin folder
"""


import pandas as pd
import numpy as np
import altair as alt
# alt.renderers.enable('notebook') # if in jupyter

df = pd.read_csv("tasks.csv")
df["Start date"] = pd.to_datetime(df["Start date"])
df["End date"] = pd.to_datetime(df["End date"])

chart = alt.Chart(df.drop("Resources", 1)).mark_bar().encode(
    x='Start date',
    x2='End date',
    y=alt.Y('Task Name', 
            sort=list(df.sort_values(["End date", "Start date"])
                                    ["Task Name"])), # Custom sorting
)

chart.save('cencoos_drifters_gantt.html')# brought this into chrome and then saved as png
