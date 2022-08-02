#%%
import xdrlib
#%%
import pandas as pd

#%%
import numpy as np


# %%
df = pd.read_csv("armenian_pubs - armenian_pubs.csv")


# %%
df.shape


# %%
df
# %%
df.info()
# %%
df_Fav_Pub = df[(df["Fav_Pub"]=="Fav_Pub")]
# %%
df

# %%
#most favourite pub 
pd.pivot_table(df,index=["Freq"],values=['Fav_Pub',],aggfunc=[np.mean,len,sum])
# %%
#the most favourite pub among female and male visitors
pd.pivot_table(df,index=["Gender"],values=["Fav_Pub", "Freq"], aggfunc=[np.mean,len,sum])


# %%
df_Fav_Pub = df[(df['Fav_Pub']== "Fav_Pub")]
# %%
#What is the age that was given most of the times
# %%
pd.pivot_table(df,index=["Age"], values=["Freq"],aggfunc=[np.mean,len,sum])
# %%
#What are most people willing to spend at the pub
# %%
pd.pivot_table(df,index=["Fav_Pub"], values=["WTS", "Freq"],aggfunc=[np.mean,len,sum])
# %%
#On which occasions visitors go to pubs most of the time?
# %%
pd.pivot_table(df,index=["Occasions"], values=["Freq"],aggfunc=[np.mean,len,sum])
# %%
df1 = pd.pivot_table(df,index=['Gender', 'Fav_Pub'], values=['Age'], aggfunc='count', fill_value= '_')
df1.sort_values('Age', ascending=False)

# %%
#save the data to csv file
df1.to_csv("armenian_pubs - armenian_pubs.csv")
# %%
