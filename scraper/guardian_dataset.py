#!/usr/bin/env python
# coding: utf-8



from nltk.tokenize import sent_tokenize, word_tokenize 
import requests
from bs4 import BeautifulSoup
import gensim

w2v = gensim.models.KeyedVectors.load_word2vec_format("scraper/w2vfile", binary=True)
def getArticle(url):
    try:
        page = requests.get(url).content
        soup = BeautifulSoup(page, features="html.parser")
        articleBody = soup.find(attrs={"itemprop":"articleBody"})
        text = articleBody.findAll('p')
        text = [i.getText() for i in text]

        out = ''
        for t in text:
            out += ' '
            out += t
        out = word_tokenize(out)
    except AttributeError:
        out = ""
    return out


def loadGuardian():


    page = requests.get("https://theguardian.com/us").content



    soup = BeautifulSoup(page, features="html.parser")
    urls = soup.findAll(attrs={"class":"fc-container__inner"})
    urls = urls[0].findAll('a')
    urls = [url.attrs['href'] for url in urls]
    urls = urls[1:]
    articles = [getArticle(url) for url in urls]
    return articles



def article2vec(words):
    converted_article = list()
    for word in article:
        try:
            converted_article.append(w2v[word])
        except KeyError:
            pass
    converted_data.append(converted_article)
    return converted_article


def guardianVectors():
    data = loadGuardian()
    converted_data = [article2vec(article) for article in data]
    return converted_data
