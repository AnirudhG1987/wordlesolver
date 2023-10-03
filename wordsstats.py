import numpy as np
import pandas as pd

df = pd.read_excel('wordsfive.xlsx')
array = np.asarray(df)
array = array.reshape(5756)[:-1]
characters_df = pd.DataFrame()

dict_char = {}
for word in array:
    for i in range(5):
        if word[i] in dict_char.keys():
            dict_char[word[i]]+=1
        else:
            dict_char[word[i]] = 1
#print(dict_char)