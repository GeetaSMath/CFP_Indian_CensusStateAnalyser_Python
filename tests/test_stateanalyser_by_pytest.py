import pytest
from indian_census_exception import IndianCensusException
from indian_census_analyser import IndianStatesCensus

class TestIndianStateCensusProblem:

    csv_file = 'C:/Users/Geetha S Matha/Desktop/IndianCensus - Sheet1.csv'
    txt_file = 'C:/Users/Geetha S Matha/Desktop/email-password-recovery-code.tx.txt'

    @pytest.fixture()
    def test_indian_states_census(self):
        data = IndianStatesCensus()
        return data

    def test_match_records(self, test_indian_states_census):
        expected = test_indian_states_census.count_records(self.csv_file)
        assert expected == 29

    def test_match_extention(self, test_indian_states_census):
        actual = test_indian_states_census.csv_file_correct(self.csv_file)
        expected = '.csv'
        assert actual == expected

    def test_unmatch_extention(self, test_indian_states_census):
        with pytest.raises(IndianCensusException) as exception:
            test_indian_states_census.csv_file_correct(self.txt_file)
        assert exception.value.message == "Invalid File Name"