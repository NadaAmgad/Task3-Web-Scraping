import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import locale
from datetime import datetime

def clean_data(df):
  '''
    Function Name: clean_data
    Funtion Description: a function to change all string values to be lower case and consistent
    Inputs:  DataFrame with dirty data
    Outputs: Clean DataFrame
  '''
  try:
      # Case Consistency and removing paddings
      for column in df:
        Data_cleaning_case_consistency(column,df)
        Data_cleaning_remove_padding(column,df)

      # Dropping Duplicates
      Data_cleaning_dropping_duplicates(df)

      # Replace commas with dots in rating
      df["Moviemeter Rating"] = df["Moviemeter Rating"].map(lambda x : float(x.replace(',','.')))

      # Getting Duration as Int in minutes
      df["Duration"] = df["Duration"].str.split().str[0].astype(int)
      return df
  
  except Exception as e:
      print(e)

def Data_cleaning_case_consistency(column,dataframe):
  '''
    Function Name: Data_cleaning_case_consistency
    Funtion Description: a function to change all string values to be lower case and consistent
    Inputs:  Dataframe with mixed upper and lower case strings, The Column that will be checked for consistency
    Outputs: Case Consistent DataFrame
  '''
  try:
    for label, row in dataframe.iterrows():
      if(type(row[column]) == str):
        dataframe.loc[label,column] = row[column].lower()
    return dataframe
  except Exception as e:
     print(e)

def Data_cleaning_remove_padding(column,dataframe):
  '''
    Function Name: Data_cleaning_remove_padding
    Funtion Description: a funtion to remove spaces befor or after a string
    Inputs: Dataframe with padded strings (Strings that may have sapces before or after), The Column that encounter removing padding
    Outputs: Dataframe with string not padded with spaces
  '''
  try:
    for label, row in dataframe.iterrows():
      if(type(row[column]) == str):
        dataframe.loc[label,column] = row[column].strip()
    return dataframe
  except Exception as e:
      print(e)

def Data_cleaning_dropping_duplicates(dataFrame):
  '''
    Function Name: Data_cleaning_dropping_duplicates
    Funtion Description: a function to remove rows that are Duplicated
    Inputs: Dataframe with duplicated rows
    Outputs: Dataframe after removing all duplicated rows
  '''
  try:
    dataFrame.drop_duplicates(inplace = True)
    return dataFrame
  except Exception as e :
      print(e)