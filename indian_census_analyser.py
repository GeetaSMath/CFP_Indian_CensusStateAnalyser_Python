import pandas as pd

def state_census_problem():
    '''This Method Is Used To Load
        The CSV File'''
    csv_data = pd.read_csv('C:/Users/Geetha S Matha/Desktop/IndianCensus - Sheet1.csv')
    print(csv_data)

def count_records():
    '''This method is used to count records from the existed records,
        the number of records present in the csv file'''
    csv_data = pd.read_csv('C:/Users/Geetha S Matha/Desktop/IndianCensus - Sheet1.csv')
    print(csv_data.shape)

list1 = count_records()
print(list1)