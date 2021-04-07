import os
import pandas as pd

##Declarando as variaveis
files = []
dir = "grupos/"
li = []

## Listando todos os arquivos do diretorio grupos
all_files = os.listdir(dir)
## Filtrando apenas por arquivos .txt
txt_files = filter(lambda x: x[-4:] == '.txt', all_files)
files = list(txt_files)

names= {'nome':str,'grupo':str, 'ra':str}
for filename in list(files):
    df = pd.read_csv(dir+filename, dtype=names,index_col=False)
    li.append(df)


grupos = pd.concat(li,axis=0, ignore_index=True)

print(grupos.sort_values(by=['grupo']))
