#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## 307multigrains
## File description:
## main
##


class ArgChecker:
    def __init__(self, args: list) -> None:
        self._args_list = list()
        if self.check_args(args) is False:
            self._args_list = None

    def check_args(self, args: list) -> bool:
        for value in args:
            try:
                tmp = int(value)
                if tmp < 0:
                    raise ValueError()
                self._args_list.append(tmp)
            except ValueError:
                print(f"ValueError at ArgChecker l.16: Value '{value}' must be a positive integer.")
                return False
        return True

    def getArgsList(self) -> list:
        return self._args_list
