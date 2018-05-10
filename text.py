import pandas as pd
import csv
import nltk as nl
import nltk.corpus as nc
import re as regex
import math
import operator
import matplotlib.pyplot as plt
import numpy as np


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
    cl = csv['Coding:Level1']
    cidx = []
    iidx = []
    aidx = []
    for i in range(len(mes)):
    # for i in range(1):
        if not isinstance(mes[i], str):
            if math.isnan(mes[i]):
                mes[i] = ""
        mes[i].strip()
        m = nl.tokenize.word_tokenize(mes[i])
        sentence = []
        for w in m:
            w = w.lower()
            if w not in stop:
                sentence.append(w)
        mes[i] = sentence
        if cl[i] == 'Information':
            iidx.append(i)
        elif cl[i] == 'Community':
            cidx.append(i)
        elif cl[i] == 'Action':
            aidx.append(i)
        # print(sentence)

    for i in range(len(cl)):
        csv['message'] = mes
    csv.to_csv("data/stopsremoved.csv", index=False)

    return mes, cl, cidx, iidx, aidx


def counts(idxlist, messages):
    countdict = {}
    for i in idxlist:
        for word in messages[i]:
            if word in countdict:
                countdict[word] += 1
            else:
                countdict[word] = 1
    sortedcounts = sorted(countdict.items(), key=operator.itemgetter(1), reverse=True)

    return sortedcounts[0:50]

def main():
    # removelinks('data/labelsmessages.csv')

    stop = nc.stopwords
    s = set(stop.words('english'))
    s.add('!')
    s.add('.')
    s.add('?')
    s.add('\n')
    s.add('\\n')
    s.add('\\n\\n')
    s.add('\\n\\nwe')
    s.add('\\nwe')
    s.add('@')
    s.add('\'')
    s.add(',')
    s.add(';')
    s.add(':')
    s.add('(')
    s.add(')')
    s.add('#')
    s.add('...')
    s.add("'s")
    s.add("n't")
    s.add('``')
    s.add("''")
    s.add("'re")
    s.add('de')
    mes, cl, cidx, iidx, aidx = removestop('data/linksremoved.csv', s)

    iwords = counts(iidx, mes)
    awords = counts(aidx, mes)
    cwords = counts(cidx, mes)
    l = [i for i in range(len(mes))]
    entire = counts(l, mes)

    fontscale = iwords[0][1] + iwords[-1][1]
    iwords = dict(iwords)

    fonts = []
    icolors = []
    idict = {}
    for key, value in zip(iwords.keys(), iwords.values()):
        fonts.append((key, 40 * value / fontscale))
        icolors.append(value / fontscale)
        idict[key] = value / fontscale
    xs = [x for x in np.arange(1/8, 1, 1/4)]
    ys = [y for y in np.arange(9/10, 0, -1/10)]
    for i in range(len(xs)):
        for j in range(len(ys)):
            plt.text(xs[i], ys[j], s=fonts[i * len(ys) + j][0], fontsize=fonts[i * len(ys) + j][1], ha='center', va='center',
                     color=(icolors[i * len(ys) + j], 0, 0))
    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.title("Information Most Popular Words")
    plt.savefig('imgs/I_words.png')
    plt.show()
    plt.clf()

    fontscale = awords[0][1] + awords[-1][1]
    awords = dict(awords)

    fonts = []
    acolors = []
    adict = {}
    for key, value in zip(awords.keys(), awords.values()):
        fonts.append((key, 40 * value / fontscale))
        acolors.append(value / fontscale)
        adict[key] = value / fontscale
    xs = [x for x in np.arange(1/8, 1, 1/4)]
    ys = [y for y in np.arange(9/10, 0, -1/10)]
    for i in range(len(xs)):
        for j in range(len(ys)):
            plt.text(xs[i], ys[j], s=fonts[i * len(ys) + j][0], fontsize=fonts[i * len(ys) + j][1], ha='center', va='center',
                     color=(0, acolors[i * len(ys) + j], 0))
    ax = plt.gca()
    plt.title("Action Most Popular Words")
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.savefig('imgs/A_words.png')
    plt.show()
    plt.clf()

    fontscale = cwords[0][1] + cwords[-1][1]
    cwords = dict(cwords)

    fonts = []
    ccolors = []
    cdict = {}
    for key, value in zip(cwords.keys(), cwords.values()):
        fonts.append((key, 40 * value / fontscale))
        ccolors.append(value / fontscale)
        cdict[key] = value / fontscale
    xs = [x for x in np.arange(1/8, 1, 1/4)]
    ys = [y for y in np.arange(9/10, 0, -1/10)]
    for i in range(len(xs)):
        for j in range(len(ys)):
            plt.text(xs[i], ys[j], s=fonts[i * len(ys) + j][0], fontsize=fonts[i * len(ys) + j][1], ha='center', va='center',
                     color=(0, 0, ccolors[i * len(ys) + j]))
    ax = plt.gca()
    plt.title("Community Most Popular Words")
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.savefig('imgs/C_words.png')
    plt.show()
    plt.clf()

    fontscale = entire[0][1] + entire[-1][1]
    entire = dict(entire)

    fonts = []
    ecolors = []
    for key, value in zip(entire.keys(), entire.values()):
        fonts.append((key, 40 * value / fontscale))
        r = 0
        g = 0
        b = 0
        if key in idict:
            r = idict[key]
        if key in adict:
            g = adict[key]
        if key in cdict:
            b = cdict[key]
        ecolors.append((r, g, b))
    xs = [x for x in np.arange(1/8, 1, 1/4)]
    ys = [y for y in np.arange(9/10, 0, -1/10)]
    for i in range(len(xs)):
        for j in range(len(ys)):
            plt.text(xs[i], ys[j], s=fonts[i * len(ys) + j][0], fontsize=fonts[i * len(ys) + j][1], ha='center', va='center',
                     color=(ecolors[i * len(ys) + j]))
    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.title("Most Popular Words")
    plt.savefig('imgs/E_words.png')
    plt.show()
    plt.clf()


if __name__ == '__main__':
    main()
