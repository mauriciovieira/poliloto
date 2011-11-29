#!/usr/bin/env python3
# coding: utf-8

from html.parser import HTMLParser

class MegasenaParser(HTMLParser):
    title = "Resultado"
    concursos = []
    headers = []
    in_headers = False 
    def __init__(self,page="../resultados/D_MEGA.HTM"):
        page = open(page, encoding = 'iso-8859-1').read()
        HTMLParser.__init__(self)
        self.feed(page)

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        if tag == 'tr':
            self.line = []
        elif tag == 'th':
            self.in_headers = True

    def handle_endtag(self, tag):
        if tag == 'tr':
            conc = dict(zip(self.headers, self.line))
            self.concursos.append(conc)
        elif tag == 'th':
            self.in_headers = False
        self.current_tag = None 

    def handle_data(self, data):
        if self.current_tag == 'title':
            self.title = data
        elif self.current_tag == 'font' and self.in_headers:
            self.headers.append(data)
        elif self.current_tag == 'td':
            self.line.append(data)
        else:
            pass

if __name__ == '__main__':
    mp = MegasenaParser() 
    print(mp.concursos)
