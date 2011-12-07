# coding: utf-8

from HTMLParser import HTMLParser
from datetime import datetime

class LoteriasParser(HTMLParser):
    def __init__(self,page):
        self.title = "Resultado"
        self.concursos = []
        self.headers = []
        self.in_headers = False #flag de estado
        page = open(page).read()
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
            v = data
            if v.find(",") > -1:
                v = float(v.replace(".","").replace(",","."))
            elif v.find("/") > -1:
                v = datetime.strptime(v,"%d/%m/%Y")
            else:
                try:
                    v = int(v)
                except ValueError, e:
                    pass
            self.line.append(v)
        else:
            pass


class MegasenaParser(LoteriasParser):
    def __init__(self,page="../resultados/D_MEGA.HTM"):
        self.apostas = [ x for x in map(lambda s: "%dª Dezena" %s, range(1,7)) ]
        self.floats = ['Rateio_Sena']
        LoteriasParser.__init__(self,page)

class LotofacilParser(LoteriasParser):
    
    def __init__(self,page="../resultados/D_LOTFAC.HTM"):
        self.apostas = [ x for x in map(lambda s: "Bola%d" % s, range(1,16)) ]
        LoteriasParser.__init__(self,page)

if __name__ == '__main__':
    mp = MegasenaParser()
    lp = LotofacilParser()
    from pprint import pprint
    pprint(mp.concursos)
