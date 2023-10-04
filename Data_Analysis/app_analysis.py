import pandas as pd
import matplotlib.pyplot as plt
from data_analysis_module import *
from data_cleaning_module import *
import os

combined_data_dataframe = pd.read_csv(os.path.abspath('../src/combined_data.csv'))

print('######################################################')
print('Combined Data Frame :')
print(combined_data_dataframe)
df_cd = clean_data(combined_data_dataframe)

print('######################################################')
print('Cleaned Data Frame :')
print(df_cd)

print('######################################################')
print('Outliers Plot :')
outliers_plot(df_cd,'Moviemeter Rating','Year')
outliers_plot(df_cd,'IMDB Rating','Year')

#MovieMeter Top
print('######################################################')
print('Moviemeter Top Rated :')
print(top_rated(df_cd,5,col='Moviemeter Rating'))

#IMDB Top
print('######################################################')
print('IMDB Top Rated :')
print(top_rated(df_cd,5,col='IMDB Rating'))

#MovieMeter Top Reversed
print('######################################################')
print('Moviemeter Top Reversed :')
print(top_rated(df_cd,5,col='Moviemeter Rating',reverse=True))

#IMDB Top Reversed
print('######################################################')
print('IMDB Top Reversed :')
print(top_rated(df_cd,5,col='IMDB Rating',reverse=True))

print('######################################################')
print('Movies Per Decade :')
print(movies_per_decade(df_cd))

print('######################################################')
print('Rating Distribution :')
rating_distribution(df_cd)


most_common = most_common_movie_genre(df_cd,col='Genre')
print('######################################################')
print('The most common genre is: ' + most_common)

print('######################################################')
print('Genre Distribution :')
genre_distribution()