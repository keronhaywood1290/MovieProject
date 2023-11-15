import pandas as pd 
import imdb
import os 
import cleaner
from time import sleep
from progress.spinner import Spinner

fileName = "\\movies.csv"
path=os.getcwd() + fileName
df=pd.read_csv(fr"{path}", encoding='latin1')
df.drop_duplicates(subset=["MOVIES","YEAR"], keep='first',inplace=True)
df["YEAR"] = df.apply( lambda x: cleaner.insrt_null_row(x["MOVIES"],"year") if pd.isnull (x["YEAR"]) else cleaner.clean_year(x["YEAR"]), axis = 1)
df["STARS"]= df["STARS"].apply(lambda x: cleaner.clean_stars(x))
df["RunTime"]=df["RunTime"].astype(str)
df["RunTime"] = df.apply( lambda x: cleaner.insrt_null_row(x["MOVIES"],"runtimes") if x["RunTime"]=="nan" else cleaner.convrt_run_time(x["RunTime"]), axis = 1)
df.to_csv("Formatted_Movies.csv", encoding='latin1')





            