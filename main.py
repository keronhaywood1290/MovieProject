import pandas as pd 
import imdb
import os 
import cleaner

fileName = "\\movies.csv"
path=os.getcwd() + fileName
df=pd.read_csv(fr"{path}", encoding='latin1')
# Remove movies from the dataframe that have the same title and year
df.drop_duplicates(subset=["MOVIES","YEAR"], keep='first',inplace=True)
# call the function to clean the year column
df["YEAR"] = df.apply( lambda x: cleaner.insrt_null_row(x["MOVIES"],"year") if pd.isnull (x["YEAR"]) else cleaner.clean_year(x["YEAR"]), axis = 1)
# call the clean stars function to format the stars column 
df["STARS"]= df["STARS"].apply(lambda x: cleaner.clean_stars(x))
# convert the RunTime columns to string format and call the cleaner funtion to convert to H:MM format 
df["RunTime"]=df["RunTime"].astype(str)
df["RunTime"] = df.apply( lambda x: cleaner.insrt_null_row(x["MOVIES"],"runtimes") if x["RunTime"]=="nan" else cleaner.convrt_run_time(x["RunTime"]), axis = 1)
# add the cleaned file to CWD 
df.to_csv("Formatted_Movies.csv", encoding='latin1')





            