#%%
import pandas as pd
import numpy as np
import altair as alt
# %%
ebola = pd.read_csv("/Users/marissaboyd/Downloads/ebola_data_db_format.csv")
# %%
ebola.to_csv("/Users/marissaboyd/git/data-visualization-boyd-python/data/ebola.csv")
# %%
