##
## EPITECH PROJECT, 2021
## 307multigrains
## File description:
## test_Optimizer
##

from sources.Optimizer import Optimizer


class TestOptimizer:
    def test_successfulOptimizerCreation(self, capsys):
        tOptimizer = Optimizer([45, 41, 21, 63, 198, 259, 257, 231, 312])
        stdout = capsys.readouterr()[0]
        assert stdout is not None
        assert tOptimizer.grainsPrices == [198, 259, 257, 231, 312]
        assert tOptimizer.resources == [45, 41, 21, 63]
