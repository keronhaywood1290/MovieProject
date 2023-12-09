import imdb
ia = imdb.Cinemagoer()

# method to remove unecesarry characters from the year column 
def clean_year (year):
    cln_year=""
    for num in year:
        if num.isdigit():
            cln_year = cln_year + num
    if len(cln_year) > 4:
        fmt_year = cln_year[:4]+"-"+cln_year[4:]
        return fmt_year
    elif len(cln_year) <= 4:
        return cln_year

# method to add missing year or runtime for each movie 
# for runtimes returned by the imdb library the method calls the convrt_run_time method to change the time format to h:mm
def insrt_null_row (movie,column):
    data=""
    #Query the movie title from this cell against the IMDB library
    # take the first element to then query the year or runtime based on parameter passed to this method 
    search_movie = ia.search_movie(movie)
    movie_id = search_movie[0].movieID
    if len(search_movie)>0:
        if column=="year":  
            try:
                data = ia.get_movie(movie_id).data["year"]
                print(f"{movie}" + " year_inserted")
            except:
                data = ""

        else:
            try:
                runtime = ia.get_movie(movie_id).data["runtimes"][0]
                data = convrt_run_time(runtime)
                print(f"{movie}" + " runtime_inserted")
            except:
                data=""
        return data
    else:
        return ""
        
# method to clean the stars column by removing extra spaces
def clean_stars (stars):
    char_remov = ["    ","|"]
    for char in char_remov:
        stars = stars.replace(char, "")
    return stars

# method to convert runtime for reach rows' run time from mm format to h:mm 
def convrt_run_time (time_arg):
    if '.' in time_arg:
        time_arg=time_arg.split('.')[0]

    time=int(time_arg)
    cnvrt_time = ""
    if time<60:
        cnvrt_time = str(time) + "m"
    elif time%60==0:
        hr = int (time/60)
        cnvrt_time = str(hr) + "h"
    else:
        min = int (time%60)
        hr = int (time/60)
        cnvrt_time = f"{hr}h {min}m"
    return cnvrt_time


