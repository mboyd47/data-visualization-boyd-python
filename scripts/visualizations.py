
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
countries = ['Guinea','Liberia','Sierra Leone']
deaths = deaths[deaths.Country.isin(countries)]
cases = cases[cases.Country.isin(countries)]
#%%
deaths = deaths.rename(columns = {'value':'death_count'}).drop(columns = ['Unnamed: 0'])
cases = cases.rename(columns = {'value':'case_count'}).drop(columns = ['Unnamed: 0'])
all = pd.merge(deaths, cases, how = 'outer', on = ['Date','Country']).drop(columns = ['Indicator_x','Indicator_y'])
#%%
#dot plot with raw counts
alt.Chart(deaths[deaths.death_count != 0]).mark_circle(opacity=1).encode(
    alt.X('Date:T'),
    alt.Y('death_count'),
    alt.Color('Country'),
    alt.Facet('Country')
).resolve_scale(
    y='independent'
)
# %%
#line plot with raw counts
chart1 = (alt.Chart(deaths[deaths.death_count != 0]).mark_line(opacity=1).encode(
            alt.X('Date:T'),
            alt.Y('death_count'),
            alt.Color('Country', scale = alt.Scale(
            domain=['Guinea', 'Liberia', 'Sierra Leone'],
            range=['black', 'dark grey','grey']))
            ))
# %%
#basic area chart with raw counts
chart2 = (alt.Chart(cases[cases.case_count != 0]).mark_area(opacity=1).encode(
            alt.X('Date:T'),
            alt.Y('case_count'),
            alt.Color('Country')
            ))
# %%
#first attempt at layered chart in altair
line = (alt.Chart(all).mark_line(opacity=1).encode(
            alt.X('Date:T'),
            alt.Y('death_count', title = 'Count of Deaths'),
            alt.Color('Country')
        ))
area = (alt.Chart(all).mark_area(opacity = .5).encode(
    alt.X('Date:T'),
    alt.Y('case_count', title = 'Count of Cases'),
    alt.Color('Country')
))
alt.layer(area,line).properties(
    title = 'Ebola Case and Death Counts by Country',
    )
#%%
# Layered Chart in Altair showing case and death counts 
# by country over time
base = alt.Chart(all).encode(
    alt.X('Date:T', axis = alt.Axis(title=None))
)
area = base.mark_area(opacity=0.3).encode(
    alt.Y('case_count', axis = alt.Axis(title = 'Count of Cases (Area)')),
    alt.Color('Country')
)
line = base.mark_line(interpolate='monotone').encode(
    alt.Y('death_count', axis=alt.Axis(title='Deaths (Lines)')),
    alt.Color('Country')
)
labels = base.mark_text(align='left', dx=5).encode(
    x='max(Date):T',
    y=alt.Y('death_count', aggregate={'argmax': 'Date'}),
    text='Country:N',
    color='Country:N'
)
alt.layer(area, line, labels).properties(title = 'A Visualization of the Ebola Outbreak, 2014-2015')
# %%