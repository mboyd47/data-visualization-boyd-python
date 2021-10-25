
#%%
import pandas as pd
import numpy as np
import altair as alt
#%%
deaths = pd.read_csv("/Users/marissaboyd/git/data-visualization-boyd-python/data/deaths.csv")
cases = pd.read_csv("/Users/marissaboyd/git/data-visualization-boyd-python/data/cases.csv")
ebola = pd.read_csv("/Users/marissaboyd/git/data-visualization-boyd-python/data/ebola.csv")
world_pop = pd.read_csv("/Users/marissaboyd/git/data-visualization-boyd-python/data/world_pop.csv")
#%%
#dot plot with raw counts
alt.Chart(deaths[deaths.value != 0]).mark_circle(opacity=1).encode(
    alt.X('Date:T'),
    alt.Y('value'),
    alt.Color('Country'),
    alt.Facet('Country')
).resolve_scale(
    y='independent'
)
# %%
#area plots with raw counts
alt.Chart(deaths[deaths.value != 0]).mark_area(opacity=1).encode(
    alt.X('Date:T'),
    alt.Y('value'),
    alt.Color('Country'),
    alt.Facet('Country')
)