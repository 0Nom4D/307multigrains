#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## 307multigrains
## File description:
## Optimizer
##

from sources.DantzigMatrix import DantzigMatrix


class Optimizer:
    def __init__(self, values: list) -> None:
        self.resources = values[:4]
        self.grainsPrices = values[4:]
        self._matrix = DantzigMatrix(values)

        self._matrix.displayMatrix()
        while self._matrix.checkGaussEnd():
            print()
            self._matrix.applyPivot(self._matrix.getPivot())
            self._matrix.displayMatrix()
            print()
            print()
        self._displaysRessources()
        self._displaysProduction()
        pass

    def _displaysRessources(self) -> None:
        print(f"Resources: {self.resources[0]} F1, {self.resources[1]} F2, {self.resources[2]} F3,"
              f" {self.resources[3]} F4", end='\n\n')

    def _displaysProduction(self) -> None:
        grains = ["Oat", "Wheat", "Corn", "Barley", "Soy"]
        index = int(0)

        for grain in grains:
            if self._matrix.getProd(grain) == -1:
                print(f"{grain}: 0 units at ${self.grainsPrices[index]}/unit")
            else:
                print(f"{grain}: {self._matrix.getProd(grain):.2f} units at ${self.grainsPrices[index]}/unit")
            index += 1
        print()
        print(f"Total production value: ${self._matrix.getTotalProd():.2f}")
