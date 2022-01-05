#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## 307multigrains
## File description:
## DantzigMatrix
##

from typing import Any


def _createMatrix(infos: list) -> list:
    matrix = list()

    matrix.append([infos[0], 1, 0, 1, 0, 2, 1, 0, 0, 0])
    matrix.append([infos[1], 1, 2, 0, 1, 0, 0, 1, 0, 0])
    matrix.append([infos[2], 2, 1, 0, 1, 0, 0, 0, 1, 0])
    matrix.append([infos[3], 0, 0, 3, 1, 2, 0, 0, 0, 1])
    matrix.append([0, -infos[4], -infos[5], -infos[6], -infos[7], -infos[8], 0, 0, 0, 0])
    return matrix


class DantzigMatrix:
    def __init__(self, infos: list) -> None:
        self._basesStrings = ["Oat", "Wheat", "Corn", "Barley", "Soy"]
        self.matrix = _createMatrix(infos)
        self.bases = [None, None, None, None]
        pass

    def displayMatrix(self) -> None:
        for value in self.matrix:
            print(value)

    def getPivot(self):
        lowestPrice = min(self.matrix[-1])
        lowestPriceIdx = self.matrix[-1].index(lowestPrice)

        storageValues = list()
        for i in range(0, len(self.matrix) - 1):
            if self.matrix[i][lowestPriceIdx] == 0:
                continue
            storageValues.append((self.matrix[i][0] / self.matrix[i][lowestPriceIdx], (i, lowestPriceIdx)))
        pivot = [tup for tup in storageValues if tup[0] == min(storageValues)[0]]
        return pivot[0]

    def applyPivot(self, pivotInfos) -> None:
        self.bases[pivotInfos[1][0]] = self._basesStrings[pivotInfos[1][1] - 1]
        pivotValue = self.matrix[pivotInfos[1][0]][pivotInfos[1][1]]
        for i in range(len(self.matrix[pivotInfos[1][0]])):
            self.matrix[pivotInfos[1][0]][i] /= pivotValue
        for i in range(len(self.matrix)):
            if i == pivotInfos[1][0]:
                continue
            pivotValue = self.matrix[i][pivotInfos[1][1]]
            for j in range(len(self.matrix[-1])):
                self.matrix[i][j] -= pivotValue * self.matrix[pivotInfos[1][0]][j]

    def checkGaussEnd(self) -> bool:
        return any(n < 0 for n in self.matrix[-1])

    def getProd(self, grain: str) -> float:
        if grain not in self.bases:
            return -1
        return self.matrix[self.bases.index(grain)][0]

    def getTotalProd(self) -> float:
        return self.matrix[-1][0]

    def getOrder(self) -> list:
        return self.bases
