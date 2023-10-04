import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import locale
from datetime import datetime

list_of_counts=[]
def top_rated(df,n=10,reverse=False,col='Moviemeter Rating'):
    '''
        Function Name: top_rated
        Funtion Description: A function that get top rated n movies
        Inputs: DataFrame and column name that is represented by the Rating and Optional(Reverse)
        Outputs: DataFrame of Top Rated Movies Record
    '''
    try:
        df_sorted = df.sort_values(col,ascending=reverse)
        return df_sorted.iloc[0:n]['Name']
    except Exception as e:
        print(e)

def movies_per_decade(df, date_col = 'Year'):
    '''
        Function Name: movies_per_decade
        Funtion Description: A function that Count movies created for each decade
        Inputs: DataFrame and column name that is represented by the year
        Outputs: Series of counts for each decade
    '''
    try :
        df['Decade'] = (df[date_col]/10).astype(int) * 10
        return df.groupby('Decade')['Decade'].count()
    except Exception as e :
        print(e)

def rating_distribution(df,col = 'IMDB Rating'):
    try:
        df[col].hist(bins=[8,8.2,8.4,8.6,8.8,9.0])
        plt.show()
        plt.clf()
    except Exception as e:
        print(e)

def count_occurence_of_genre(column,dataframe,keyword):
    '''
        Function Name: Count_Occurence_of_keyword
        Funtion Description: A function that calculates the occurence of a specific keyword in a given column
        Inputs: A dataframe, column name and the keyword that's needed to count its occurence
        Outputs: A tuple containing the keyword and how many times it occured in the column
    '''
    try:
        count = 0
        for value in dataframe[column]:
            if keyword in value.capitalize():
                count +=1

        return (count,keyword)
    
    except Exception as e:
        print(e)

def most_common_movie_genre(dataframe,col='Genre'):
    '''
        Function Name: most_common_movie_genre
        Funtion Description: A function that returns the most common genre in the dataset
        Inputs: A dataframe, column name and list of all possible genres
        Outputs: The most common genre as a string
    '''
    try:
        movie_genres = ['Drama','Crime','Fantasy','Adventure','War','Thriller','History','Comedy','Action','Mystery','Biography','Western','Scifi','Animation','Family','Horror','Romance','Filmnoir','Sport','Music']
        for genre in movie_genres:
            count_genre = count_occurence_of_genre(col,dataframe,genre)
            list_of_counts.append(count_genre)

        # getting the most common genre from the list of tuples
        most_found_genre = max(list_of_counts)[1]
        return most_found_genre
    except Exception as e:
        print(e)

def genre_distribution():
    '''
        Function Name: genre_distribution
        Funtion Description: A function that plot a bar chart of the genre distribution
        Inputs: No inputs
        Outputs: No returns
    '''
    try:
        x_list = []
        y_list = []
        for x,y in list_of_counts:
            x_list.append(x)
            y_list.append(y)

        plt.bar(y_list, x_list,width=0.5)
        plt.xticks(rotation='vertical')
        plt.show()
    except Exception as e:
        print(e)

def outliers_plot(df,x,y):
    '''
        Function Name: outliers_plot
        Funtion Description: A function that plot outliers
        Inputs: DataFrame and x column name and y column name
        Outputs: No returns
    '''
    try:
        plt.tick_params(left = False, right = False , labelleft = False)
        plt.scatter(df[x],df[y])
        plt.title('Finding Outliers in ' + x)
        plt.show()
        plt.clf()
    except Exception as e:
        print(e)

def remove_outliers(df,criteria,ql,qh):
    '''
        Function Name: remove_outliers
        Funtion Description: A function that remove outliers
        Inputs: DataFrame and percentages of quantiles
        Outputs: No returns
    '''
    try:
        q_low = df[criteria].quantile(ql)
        q_hi  = df[criteria].quantile(qh)
        df = df[(df[criteria] < q_hi) & (df[criteria] > q_low)]
        return df
    except Exception as e:
        print(e)