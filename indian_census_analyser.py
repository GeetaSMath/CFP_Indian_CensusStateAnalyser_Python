import pandas as pd

def state_census_problem():
    csv_data = pd.read_csv('C:/Users/Geetha S Matha/Desktop/IndianCensus - Sheet1.csv')
    print(csv_data.shape)
    print(csv_data)


list = state_census_problem()

print(list)