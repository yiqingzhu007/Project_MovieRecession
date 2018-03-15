import pandas as pd
import numpy as np

preboxDF = pd.read_csv('../Data/pre_gross.csv')
preplotDF = pd.read_csv('../Data/pre_plot.csv')
mergedDF_pre = pd.merge(preboxDF,preplotDF, on=['id'])
pre25DF = mergedDF_pre[mergedDF_pre['gross']>=30000000]
pre25DF.to_csv('../Data/pre_popular.csv', index = False)


postboxDF = pd.read_csv('../Data/post_gross.csv')
postplotDF = pd.read_csv('../Data/post_plot.csv')
mergedDF_post = pd.merge(postboxDF,postplotDF, on=['id'])
post25DF = mergedDF_post[mergedDF_post['gross']>=30000000]
post25DF.to_csv('../Data/post_popular.csv', index = False)
