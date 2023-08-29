#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    s = input("Введите предложение: ")
    index = s.find("чу")
    if index == -1:
        index = s.find("щу")
    if index != -1:
        print("Буквосочетание найдено, порядковый номер первой буквы: ", index)
    else:
        print("Буквосочетание не найдено")
        