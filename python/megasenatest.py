#!/usr/bin/env python3

import unittest
from parsers import MegasenaParser

class MegasenaTest(unittest.TestCase):
    parser = MegasenaParser("../resultados/D_MEGA.HTM")
    def test_primeira_frase(self):
        '''A primeira frase deve ser "Resultado da Mega-sena"'''
        self.assertEqual(self.parser.title, "Resultado da Mega-sena")

    def test_data_primeiro_concurso(self):
        '''O primeiro concurso foi em 11/03/1996'''
        self.assertEqual(self.parser.concursos[1]['Data Sorteio'],'11/03/1996')

    def test_resultado_concurso_11(self):
        '''O resultado do concurso 11 foi 15.591.365,07'''
        res = '15.591.365,07'
        self.assertEqual(self.parser.concursos[11]['Rateio_Sena'],res)

if __name__ == '__main__':
    unittest.main()
