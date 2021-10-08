#%%
import pandas as pd
import numpy as np
import altair as alt
# %%
#importing data
ebola = pd.read_csv("/Users/marissaboyd/Downloads/ebola_data_db_format.csv")
# %%
#saved data to data folder
#ebola.to_csv("/Users/marissaboyd/git/data-visualization-boyd-python/data/ebola.csv")
# %%
ebola['Date'] = pd.to_datetime(ebola.Date)
ebola = ebola[ebola.Date != '2016-03-23']
deaths = ebola[ebola.Indicator == 'Cumulative number of confirmed, probable and suspected Ebola deaths'].reset_index(drop=True)
cases = ebola[ebola.Indicator == 'Cumulative number of confirmed, probable and suspected Ebola cases'].reset_index(drop=True)
# %%
alt.Chart(deaths[deaths.value != 0]).mark_point().encode(
    x = 'Date',
    y = 'value',
    color = 'Country',
    facet = 'Country'
).resolve_scale(
    y='independent'
)
# %%
