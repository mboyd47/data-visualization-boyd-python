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
ebola = ebola.loc[ebola['Country'] != 'Liberia 2', ['Indicator','Country','Date','value']]
#%%
world_pop_2014 = pd.DataFrame(world_pop['Year_2014'])
world_pop_2015 = pd.DataFrame(world_pop['Year_2015'])
countries = pd.DataFrame(world_pop['Country'])
world_pop2 = pd.concat([countries, world_pop_2014, world_pop_2015], axis=1)
# %%
ebola['Date'] = pd.to_datetime(ebola.Date)
ebola = ebola[ebola.Date != '2016-03-23']
deaths = ebola[ebola.Indicator == 'Cumulative number of confirmed, probable and suspected Ebola deaths'].reset_index(drop=True)
cases = ebola[ebola.Indicator == 'Cumulative number of confirmed, probable and suspected Ebola cases'].reset_index(drop=True)
#%%
alt.Chart(deaths[deaths.value != 0]).mark_circle(opacity=1).encode(
    alt.X('Date:T'),
    alt.Y('value'),
    alt.Color('Country'),
    alt.Facet('Country')
).resolve_scale(
    y='independent'
)
# %%
world_pop2 = world_pop2.assign(avg_pop = lambda world_pop2: (world_pop2.Year_2014 + world_pop2.Year_2015)/2)
# %%
pd.crosstab(index=ebola['Country'],columns='value')
# %%
guinea_pop = world_pop2.query('Country == "Guinea"')['avg_pop']
liberia_pop = world_pop2.query('Country == "Liberia"')['avg_pop']
mali_pop =  world_pop2.query('Country == "Mali"')['avg_pop']
nigeria_pop =  world_pop2.query('Country == "Nigeria"')['avg_pop']
sierra_leone_pop =  world_pop2.query('Country == "Sierra Leone"')['avg_pop']
us_pop =  world_pop2.query('Country == "United States of America"')['avg_pop']
#%%
#gprop = (deaths.query('Country == "Guinea"')['value'])/guinea_pop

# %%
death_pop = pd.DataFrame({"Country": ['Guinea','Liberia','Mali','Nigeria',
                            'Sierra Leone','United States of America'],
                        "Prop":[]})