#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    word = input("Введите слово с точкой в конце: ")
    num = int(input("Введите номер буквы, после которой нужно вставить новую букву: "))
    letter = input("Введите букву, которую нужно вставить: ")

    new_word = word[:num] + letter + word[num:]
    print("Новое слово:", new_word)