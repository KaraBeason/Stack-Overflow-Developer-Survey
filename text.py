import pandas as pd
import csv
import nltk as nl
import nltk.corpus as nc
import re as regex
import math


def removelinks(csvpath):
    csv = pd.read_csv(csvpath)

    mes = csv['message']
    for i in range(len(mes)):
        if "http" in mes[i] or "www" in mes[i]:
            mes[i] = regex.sub("http\S+", "", mes[i])
            mes[i] = regex.sub("www\S+", "", mes[i])

    csv['message'] = mes
    csv.to_csv("data/linksremoved.csv", index=False)

def removestop(csvpath, stop):
    csv = pd.read_csv(csvpath)
    mes = csv['message']

    for i in range(len(mes)):
    # for i in range(1):
        if not isinstance(mes[i], str):
            if math.isnan(mes[i]):
                mes[i] = ""
        mes[i].strip()
        m = nl.tokenize.word_tokenize(mes[i])
        sentence = []
        for w in m:
            if w not in stop:
                sentence.append(w)
        mes[i] = sentence
        # print(sentence)

    csv['message'] = mes
    csv.to_csv("data/stopsremoved.csv", index=False)


def main():
    # removelinks('data/labelsmessages.csv')

    # stop = nc.stopwords
    # s = set(stop.words('english'))
    # s.add('!')
    # s.add('.')
    # s.add('?')
    # s.add('\n')
    # s.add('\\n')
    # s.add('\\n\\n')
    # s.add('@')
    # s.add('\'')
    # s.add(',')
    # s.add(';')
    # s.add(':')
    # s.add('(')
    # s.add(')')
    # s.add('#')
    # s.add('...')
    # s.add("'s")
    # s.add("n't")
    # print(s)
    # removestop('data/linksremoved.csv', s)

    csv = pd.read_csv('data/stopsremoved.csv')
    mes = csv['message']


if __name__ == '__main__':
    main()

