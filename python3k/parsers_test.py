#!/usr/bin/env python3

import unittest
from parsers import MegasenaParser

class MegasenaTest(unittest.TestCase):

    html = '''<table border="0" cellspacing="1" cellpadding="0" width="1810">
        <tr>
        <th><font>Concurso</font></th>
        <th><font>Data Sorteio</font></th>
        <th><font>1ª Dezena</font></th>
        <th><font>2ª Dezena</font></th>
        <th><font>3ª Dezena</font></th>
        <th><font>4ª Dezena</font></th>
        <th><font>5ª Dezena</font></th>
        <th><font>6ª Dezena</font></th>
        <th><font>Arrecadacao_Total</font></th>
        <th><font>Ganhadores_Sena</font></th>
        <th><font>Cidade</font></th>
        <th><font>UF</font></th>
        <th><font>Rateio_Sena</font></th>
        <th><font>Ganhadores_Quina</font></th>
        <th><font>Rateio_Quina</font></th>
        <th><font>Ganhadores_Quadra</font></th>
        <th><font>Rateio_Quadra</font></th>
        <th><font>Acumulado</font></th>
        <th><font>Valor_Acumulado</font></th>
        <th><font>Estimativa_Prêmio</font></th>
        <th><font>Acumulado_Mega_da_Virada</font></th>
        </tr>
        <tr>
        <td rowspan="1">1</td>
        <td rowspan="1">11/03/1996</td>
        <td rowspan="1">41</td>
        <td rowspan="1">05</td>
        <td rowspan="1">04</td>
        <td rowspan="1">52</td>
        <td rowspan="1">30</td>
        <td rowspan="1">33</td>
        <td rowspan="1">0,00</td>
        <td rowspan="1">0</td>
        <td rowspan="1">&nbsp</td>
        <td rowspan="1"> </td>
        <td rowspan="1">0,00</td>
        <td rowspan="1">17</td>
        <td rowspan="1">39.158,92</td>
        <td rowspan="1">2016</td>
        <td rowspan="1">330,21</td>
        <td rowspan="1">SIM</td>
        <td rowspan="1">1.714.650,23</td>
        <td rowspan="1">0,00</td>
        <td rowspan="1">0,00</td>
        </tr>'''

    def test_primeira_frase(self):
        '''A primeira frase deve ser "Resultado da Mega-sena"'''

        parser = MegasenaParser(url="../resultados/d_mega.htm")
        self.assertEqual(parser.title, "Resultado da Mega-sena")

    def test_data_primeiro_concurso(self):
        '''O primeiro concurso foi em 11/03/1996'''

        parser = MegasenaParser(url="../resultados/d_mega.htm")
        self.assertEqual(parser.results[1]['Data Sorteio'], '11/03/1996')

    def test_resultado_concurso_24(self):
        '''O resultado do concurso 24 foi 18.661.679,61'''

        parser = MegasenaParser(url="../resultados/d_mega.htm")
        amount_sena = '18.661.679,61'
        self.assertEqual(parser.results[24]['Rateio_Sena'], amount_sena)

    def test_headers_from_html(self):
        parser = MegasenaParser(html=self.html)
        parsed_headers = [
            'Concurso',
            'Data Sorteio',
            '1ª Dezena',
            '2ª Dezena',
            '3ª Dezena',
            '4ª Dezena',
            '5ª Dezena',
            '6ª Dezena',
            'Arrecadacao_Total',
            'Ganhadores_Sena',
            'Cidade',
            'UF',
            'Rateio_Sena',
            'Ganhadores_Quina',
            'Rateio_Quina',
            'Ganhadores_Quadra',
            'Rateio_Quadra',
            'Acumulado',
            'Valor_Acumulado',
            'Estimativa_Prêmio',
            'Acumulado_Mega_da_Virada'
        ]
        self.assertEqual(parser.headers, parsed_headers)

    def test_results(self):
        parser = MegasenaParser(html=self.html)
        self.assertEqual(parser.results[1]['Rateio_Quina'], '39.158,92')

if __name__ == '__main__':
    unittest.main()
