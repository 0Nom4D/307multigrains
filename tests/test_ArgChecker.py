##
## EPITECH PROJECT, 2021
## 307multigrains
## File description:
## test_ArgChecker
##

from sources.ArgChecker import ArgChecker
from sources.exitCode import exitCode


class TestExitCodes:
    def test_okCode(self):
        assert not exitCode.OK

    def test_errorCode(self):
        assert exitCode.ERROR == 84


class TestArgChecker:
    def test_BadArgumentType(self, capsys):
        tChecker = ArgChecker(["a", "a", "a", "a", "a", "a", "a", "a", "a"])
        stdout = capsys.readouterr()[0]
        assert stdout == "ValueError at ArgChecker l.16: Value 'a' must be a positive integer.\n"
        assert tChecker.getArgsList() is None

    def test_NegativeArg(self, capsys):
        tChecker = ArgChecker(["10", "100", "10", "0", "200", "200", "200", "200", "-200"])
        stdout = capsys.readouterr()[0]
        assert stdout == "ValueError at ArgChecker l.16: Value '-200' must be a positive integer.\n"
        assert tChecker.getArgsList() is None

    def test_ValidArgs(self):
        tChecker = ArgChecker(["10", "100", "10", "0", "200", "200", "200", "200", "200"])
        assert tChecker.getArgsList() is not None
