from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def search_results(text, PHONE_RE):
    phones = []

    for result in re.findall(PHONE_RE, text):
        if result not in phones:
            phones.append(result)

    return phones    

def seven(text, phones):

    PHONE_RE = re.compile(r'\D(\+7\d{9,10})\D')

    result = search_results(text, PHONE_RE)

    for phone in result:
        phone = re.sub(r'\+', '', phone)
        phone = phone.replace('7', '8', 1)

        if phone not in phones:
            phones.append(phone)

    return phones

def eight(text, phones):
    PHONE_RE = re.compile(r'>(8\d{9,10})\D')

    result = search_results(text, PHONE_RE)

    for phone in result:
        if phone not in phones:
            phones.append(phone)

    return phones

def urban(text, phones):
    PHONE_RE = re.compile(r'>(\d{6,7})\D')

    result = search_results(text, PHONE_RE)

    for i in range(len(result)):
        result[i] = "8495" + result[i]
        if result[i] not in phones:
            phones.append(result[i])

    return phones

def parse(elem):
    text = str(urlopen(elem).read(),'utf-8')

    text = re.sub(' ', '', text)
    text = re.sub('-', '', text)
    text = re.sub(r'\(', '', text)
    text = re.sub(r'\)', '', text)

    phones = []

    phones = seven(text, phones)
    phones = eight(text, phones)
    phones = urban(text, phones)

    return(phones)