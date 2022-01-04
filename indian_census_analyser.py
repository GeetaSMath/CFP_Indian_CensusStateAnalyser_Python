import pandas as pd
from indian_census_exception import IndianCensusException


class IndianStatesCensus:

    def state_census_problem(self, file):
        '''This Method Is Used To Load
            The CSV File'''
        data = pd.read_csv(file)
        return data

    def count_records(self, file):
        '''This method is used to count
            the number of records present in the csv file'''
        data = pd.read_csv(file)
        return data.shape[0]

    def csv_file_correct(self, file):
        data = open(file)
        list1= data.name.endswith(".csv")
        if list1 == True:
            return '.csv'
        else:
            raise IndianCensusException("Invalid File Name")


if __name__ == '__main__':
    csv_data = IndianStatesCensus()
    file = 'C:/Users/Geetha S Matha/Desktop/IndianCensus - Sheet1.csv'
    print(csv_data.count_records(file))
    print(csv_data.csv_file_correct(file))
