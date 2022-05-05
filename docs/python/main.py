# %%

import pandas as pd
import numpy as np

pd.options.display.max_columns = None

# %%

port_clientes = pd.read_csv("C:/Users/Mayara Lopes/Desktop/Stone Challange/docs/datasets/portfolio_clientes.csv", sep=",")

# %%
    
def tratar_dataset(dataset):
    dataset = dataset.applymap(lambda x: x.upper() if isinstance(x, (object)) else x)
# %%
tratar_dataset(port_clientes)


# %%
port_clientes.info()
# %%
port_clientes