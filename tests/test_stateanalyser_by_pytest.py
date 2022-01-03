import pytest
from indian_census_exception import IndianCensusException
from indian_census_analyser import state_census_problem, count_records


class TestIndianStateCensusProblem:
    csv_file = 'C:/Users/Geetha S Matha/Desktop/IndianCensus - Sheet1.csv'

    @pytest.fixture()
    def test_indian_states_census(self):
        records = state_census_problem()
        return records

    def test_match_records(self, test_indian_states_census):
        expected = test_indian_states_census.count_records(self.csv_file)
        assert expected == 29
