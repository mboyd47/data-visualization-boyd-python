#%%
import pandas as pd
import numpy as np
import altair as alt
# %%
#importing data
ebola = pd.read_csv("/Users/marissaboyd/Downloads/ebola_data_db_format.csv")
world_pop = pd.read_csv("/Users/marissaboyd/Downloads/population-figures-by-country-csv_csv.csv")
# %%
#saved data to data folder
#ebola.to_csv("/Users/marissaboyd/git/data-visualization-boyd-python/data/ebola.csv")
#world_pop.to_csv("/Users/marissaboyd/git/data-visualization-boyd-python/data/world_pop.csv")
#%%
world_pop_2014 = pd.DataFrame(world_pop['Year_2014'])
world_pop_2015 = pd.DataFrame(world_pop['Year_2015'])
countries = pd.DataFrame(world_pop['Country'])
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
