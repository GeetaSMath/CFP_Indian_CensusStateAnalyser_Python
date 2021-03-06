import csv

import pandas as pd
from indian_census_exception import IndianCensusException


class IndianStatesCensus:

    def state_census_problem(self, file):
        """

        :param file: file
        :return: data
        """
        data = pd.read_csv(file)
        return data

    def count_records(self, file):
        """

        :param file: file
        :return: data.shape[0]
        """
        data = pd.read_csv(file)
        return data.shape[0]

    def csv_file_correct(self, file):
        """

        :param file: file
        :return: .csv to read extension
        """
        data = open(file)
        items= data.name.endswith(".csv")
        if items == True:
            return '.csv'
        else:
            raise IndianCensusException("Invalid File Name")

    def delimitor(self, csv_data):
        """

        :param csv_data:
        :return:
        """
        data = open(csv_data)
        sniffer = csv.Sniffer()
        sniff_data = sniffer.sniff(data.read())
        if not sniff_data.delimiter == ',':
            raise IndianCensusException("Delimitor Not Matched")
        else:
            return sniff_data.delimiter

    def header_validate(self, csv_data):
        data = open(csv_data)
        sniffer = csv.Sniffer()
        sniff_data = sniffer.has_header(data.read())
        print(sniff_data)
        if not sniff_data:
            raise IndianCensusException("Header Not Matched")
        else:
            return sniff_data


if __name__ == '__main__':
    csv_data = IndianStatesCensus()
    file = 'C:/Users/Geetha S Matha/Desktop/email-password-recovery-code.tx.txt'
    print(csv_data.header_validate(file))