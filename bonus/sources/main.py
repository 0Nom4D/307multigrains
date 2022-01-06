#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## 307multigrains
## File description:
## main
##

from sources.ArgChecker import ArgChecker
from sources.Optimizer import Optimizer
from sources.exitCode import exitCode
from sys import argv


def print_usage() -> int:
    print("USAGE")
    print("\t./307multigrains n1 n2 n3 n4 po pw pc pb ps", end='\n\n')
    print("DESCRIPTION")
    print("\tn1\tnumber of tons of fertilizer F1")
    print("\tn2\tnumber of tons of fertilizer F2")
    print("\tn3\tnumber of tons of fertilizer F3")
    print("\tn4\tnumber of tons of fertilizer F4")
    print("\tpo\tprice of one unit of oat")
    print("\tpw\tprice of one unit of wheat")
    print("\tpc\tprice of one unit of corn")
    print("\tpb\tprice of one unit of barley")
    print("\tps\tprice of one unit of soy")
    return exitCode.OK


def main():
    if len(argv) == 2 and (argv[1] == '-h' or argv[1] == '--help'):
        return print_usage()
    elif len(argv) != 10:
        return exitCode.ERROR
    grainsArgs = ArgChecker(argv[1:])
    if grainsArgs.getArgsList() is None:
        return exitCode.ERROR
    OptiEngine = Optimizer(grainsArgs.getArgsList())
    return exitCode.OK


if __name__ == "__main__":
    exit(main())
