#!/usr/bin/python

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 10:54:16 2019

@author: Diogo
"""

from bs4 import BeautifulSoup
import requests
import sys
from asterisk.agi import *


agi = AGI()
agi.verbose("python agi started")

postal_code = sys.argv[1]

code_1 = postal_code[0:4]
code_2 = postal_code[4:7]

agi.verbose(code_1)
agi.verbose(code_2)


url = "http://www.ctt.pt/feapl_2/app/open/postalCodeSearch/postalCodeSearch.jspx?cp4=" + code_1 + "&cp3=" + code_2 + "&method%3AsearchPC2=Procurar"
page = requests.get(url)
soup = BeautifulSoup(page.content, "lxml")
try:
    children = soup.find_all("div",  {"class": "highlighted-result text-left"})[0].findChildren()
except:
    print("ERROR")
    agi.set_variable('address', 'ERROR')
    sys.exit(1)

str = ""
for child in children:
    str = str + child.get_text() + ". "

agi.verbose(str)
agi.set_variable('address', str)
