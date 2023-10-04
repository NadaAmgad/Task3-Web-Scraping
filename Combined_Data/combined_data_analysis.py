import pandas as pd
import os

FILEPATH1 = os.path.abspath('../src/movie_data_moviemeter.csv')
FILEPATH2 = os.path.abspath('../src/movie_data_imdb.csv')

def combining_dataframes(filepath1,filepath2):
    '''
        Function Name: combining_dataframes
        Funtion Description: A function that Combine only movies found in both websites into a single dataset
        Inputs: filepaths of the 2 generated csv files
        Outputs: A dataframe -combinaton of the 2 files-
    '''
    movie_meter_dataframe = pd.read_csv(filepath1)
    imdb_dataframe = pd.read_csv(filepath2)

    combined_dataframe = pd.merge(movie_meter_dataframe, imdb_dataframe, on='Name')
    return combined_dataframe



new_dataframe = combining_dataframes(FILEPATH1,FILEPATH2)
new_dataframe = new_dataframe.drop('Movie Year',axis = 1)
new_dataframe.to_csv('combined_data.csv',index=False)

print(new_dataframe)