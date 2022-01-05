##
## EPITECH PROJECT, 2021
## 307multigrains
## File description:
## test_DantzigMatrix
##

from sources.DantzigMatrix import DantzigMatrix


class TestDantzigMatrix:
    def test_matrixCreation(self):
        tMatrix = DantzigMatrix([45, 41, 21, 63, 198, 259, 257, 231, 312])
        checkedMatrix = [
            [45, 1, 0, 1, 0, 2, 1, 0, 0, 0],
            [41, 1, 2, 0, 1, 0, 0, 1, 0, 0],
            [21, 2, 1, 0, 1, 0, 0, 0, 1, 0],
            [63, 0, 0, 3, 1, 2, 0, 0, 0, 1],
            [0, -198, -259, -257, -231, -312, 0, 0, 0, 0]
        ]

        assert tMatrix.matrix == checkedMatrix
        assert all(base is None for base in tMatrix.bases)

    def test_matrixDisplay(self, capsys):
        tMatrix = DantzigMatrix([45, 41, 21, 63, 198, 259, 257, 231, 312])
        checkedString = "[45, 1, 0, 1, 0, 2, 1, 0, 0, 0]\n" \
                        "[41, 1, 2, 0, 1, 0, 0, 1, 0, 0]\n" \
                        "[21, 2, 1, 0, 1, 0, 0, 0, 1, 0]\n" \
                        "[63, 0, 0, 3, 1, 2, 0, 0, 0, 1]\n" \
                        "[0, -198, -259, -257, -231, -312, 0, 0, 0, 0]\n"

        tMatrix.displayMatrix()
        stdout = capsys.readouterr()[0]
        assert stdout == checkedString

    def test_fetchingOrder(self):
        tMatrix = DantzigMatrix([45, 41, 21, 63, 198, 259, 257, 231, 312])
        assert all(x is None for x in tMatrix.getOrder())
