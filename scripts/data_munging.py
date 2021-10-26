#%%
import pandas as pd
import numpy as np
import altair as alt
# %%
#importing data
ebola = pd.read_csv("/Users/marissaboyd/Downloads/ebola_data_db_format.csv")
world_pop = pd.read_csv("/Users/marissaboyd/Downloads/population-figures-by-country-csv_csv.csv")
# %%
ebola = ebola.loc[ebola['Country'] != 'Liberia 2', ['Indicator','Country','Date','value']]
#%%
#subsetting world_pop df to only include 2014 and 2015
world_pop_2014 = pd.DataFrame(world_pop['Year_2014'])
world_pop_2015 = pd.DataFrame(world_pop['Year_2015'])
countries = pd.DataFrame(world_pop['Country'])
world_pop2 = pd.concat([countries, world_pop_2014, world_pop_2015], axis=1)
# %%
#removing outlying date and creating separate
#deaths and cases dfs
ebola['Date'] = pd.to_datetime(ebola.Date)
ebola = ebola[ebola.Date != '2016-03-23']
deaths = ebola[ebola.Indicator == 'Cumulative number of confirmed, probable and suspected Ebola deaths'].reset_index(drop=True)
cases = ebola[ebola.Indicator == 'Cumulative number of confirmed, probable and suspected Ebola cases'].reset_index(drop=True)
#%%
#averaging each country's pop over the two years
world_pop2 = world_pop2.assign(avg_pop = lambda world_pop2: (world_pop2.Year_2014 + world_pop2.Year_2015)/2)
# %%
##########################
#saved data to data folder
ebola.to_csv("/Users/marissaboyd/git/data-visualization-boyd-python/data/ebola.csv")
world_pop2.to_csv("/Users/marissaboyd/git/data-visualization-boyd-python/data/world_pop.csv")
deaths.to_csv("/Users/marissaboyd/git/data-visualization-boyd-python/data/deaths.csv")
cases.to_csv("/Users/marissaboyd/git/data-visualization-boyd-python/data/cases.csv")
##########################
#%%













#creating objects containing each contry's pop count
guinea_pop = world_pop2.query('Country == "Guinea"')['avg_pop'].values[0]
liberia_pop = world_pop2.query('Country == "Liberia"')['avg_pop'].values[0]
mali_pop =  world_pop2.query('Country == "Mali"')['avg_pop'].values[0]
nigeria_pop =  world_pop2.query('Country == "Nigeria"')['avg_pop'].values[0]
sierra_leone_pop =  world_pop2.query('Country == "Sierra Leone"')['avg_pop'].values[0]
us_pop =  world_pop2.query('Country == "United States"')['avg_pop'].values[0]
#%%
prop_conditions = [(deaths['Country'] == 'Guinea'), (deaths['Country'] == 'Liberia'),
                    (deaths['Country'] == 'Mali'), (deaths['Country'] == 'Nigeria'),
                    (deaths['Country'] == 'Sierra Leone'), (deaths['Country'] == 'United States of America')]
prop_values = [(deaths['value']/guinea_pop)*100, (deaths['value']/liberia_pop)*100,
                (deaths['value']/mali_pop)*100, (deaths['value']/nigeria_pop)*100,
                (deaths['value']/sierra_leone_pop)*100, (deaths['value']/us_pop)*100]
# %%
#creating new variable for deaths as proportion of country pop
deaths = deaths.assign(
    proportion = np.select(prop_conditions, prop_values, default=np.nan)
)
#%%
#dot plot with proportions
alt.Chart(deaths[deaths.value != 0]).mark_area(opacity=1).encode(
    alt.X('Date:T'),
    alt.Y('proportion'),
    alt.Color('Country'),
    alt.Facet('Country')
)
# %%
