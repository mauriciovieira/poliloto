#!/usr/bin/env python3
# coding: utf-8

from html.parser import HTMLParser
import json


class LotteryParser(HTMLParser):

    def __init__(self, **kwargs):
        self.title = "Resultado"
        self.results = []
        self.headers = []
        self.in_headers = False

        self.url = kwargs.get('url')
        self.html = kwargs.get('html')
        if self.url:
            results_file = open(self.url, encoding = 'iso-8859-1')
            page = results_file.read()
            results_file.close()
        elif self.html:
            page = self.html

        HTMLParser.__init__(self)
        self.feed(page)
        self.clean_up()

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        if tag == 'tr':
            self.line = []
        elif tag == 'th':
            self.in_headers = True

    def handle_endtag(self, tag):
        if tag == 'tr':
            conc = dict(zip(self.headers, self.line))
            self.results.append(conc)
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

    def to_json(self):
        return json.dumps(self.results)

    def sorteados(self, num):
        """Apostas sorteadas para o concurso num"""
        apostas = self.apostas or []
        concurso = {} if num>=len(self.results) else self.results[num]
        return set([concurso.get(x,0) for x in apostas])

    def confere(self, num, apostas):
        res = []
        if num >= len(self.results):
            res.append("Concurso %d - não aconteceu" % num )
        else:
            res.append("Concurso: %d - %s" % (num, self.results[num]['Data Sorteio']))
            res.append("\tJogos sorteados: %s" % (" ".join(sorted(self.sorteados(num)))))
            res.append("\tJogos    feitos: %s" % (" ".join(apostas)))
            acertos = self.sorteados(num).intersection(apostas)
            res.append("\t%d acertos - %s" % (len(acertos), " ".join(sorted(acertos))))
        return "\n".join(res)

    def clean_up(self):
        pass


class MegasenaParser(LotteryParser):
    apostas = [ x for x in map(lambda s: "%dª Dezena" %s, range(1,7)) ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def clean_up(self):
        """Clean up defective rows from original data"""
        if self.url:
            self.results.pop(4)


class LotofacilParser(LotteryParser):
    apostas = [ x for x in map(lambda s: "Bola%d" % s, range(1,16)) ]
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


if __name__ == '__main__':
    mp = MegasenaParser()
    from pprint import pprint
    pprint(mp.results)
    lp = LotofacilParser()
    pprint(lp.results)

