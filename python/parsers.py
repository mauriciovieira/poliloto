#!/usr/bin/env python3
# coding: utf-8

from html.parser import HTMLParser

class MegasenaParser(HTMLParser):
    title = "Resultado da Mega-senaxa"
    concursos = [{'Concurso': 1, 'Data Sorteio': '11/03/1996'},
                 {'Concurso': 2, 'Data Sorteio': '18/03/1996'},
                ]
    def __init__(self,page="../resultados/D_MEGA.HTM"):
        self.page = open(page, encoding = 'iso-8859-1').read()
        HTMLParser.__init__(self)
        self.feed(self.page)

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
    def handle_endtag(self, tag):
        self.current_tag = None 
    def handle_data(self, data):
        if self.current_tag == 'title':
            self.title = data

if __name__ == '__main__':
   mp = MegasenaParser() 
