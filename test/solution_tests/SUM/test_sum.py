import pytest

from lib.solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_negative_num(self):
        with pytest.raises(Exception):
            sum_solution.compute(-1, -2)

    def test_out_of_range_num(self):
        with pytest.raises(Exception):
            sum_solution.compute(200, 100)

