# -*- coding: utf-8 -*-

import os
import unittest
import switch_translate
from flask import json
from lib.translate import translate

class TranslitTestCase(unittest.TestCase):
    def setUp(self):
        self.text = u'ghjdthrf ищер дфтпгфпуы'

    def test_translate(self):
        result = translate(self.text)
        self.assertEqual(result, u'проверка both languages')


class Switch_tranlateTestCase(unittest.TestCase):
    def setUp(self):
        self.app = switch_translate.app.test_client()
        self.text = 'ghjdthrf ищер дфтпгфпуы'

    def test_eng(self):
        response = self.app.post('/', data=json.dumps({'text':  self.text}), content_type='application/json')
        self.assertEquals(response.get_data(), 'проверка both languages') 

      
if __name__ == '__main__':
    unittest.main()
