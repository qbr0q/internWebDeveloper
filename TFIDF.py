from typing import IO
from math import log
from DB.db_funcs import add_tfidf

def tfidf(file_name: str) -> None:
    with open(file_name, encoding='UTF-8') as file:
        words = file.read().split()
        words = list(filter(lambda x: x.isalpha(), words))
        for word in set(words):
            print(word)
            tf = get_tf(word, words)
            idf = get_idf()
            add_tfidf(word, tf, idf)

def get_tf(word: str, words: list) -> float:
    return words.count(word) / len(words)

def get_idf() -> float:
    return log(1/1) # т.к. файл один, то и кол-во файлов со словом - 1
    # (если я правильно понял задание ¯\_(ツ)_/¯)