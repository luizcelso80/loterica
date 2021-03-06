from typing import final
import requests, pprint, json, sys
from datetime import datetime

from requests import structures

PARTE1 = 'http://loterias.caixa.gov.br'
PARTE2 = 'pw/Z7_HGK818G0KG4QF0QLDEU6PK2084/res/id=buscaResultado/c=cacheLevelPage//p=concurso='
PARTE3 = '?timestampAjax=1634917125537'
args = sys.argv[1:][0]

try:

    response = requests.get('http://loterias.caixa.gov.br/wps/portal/loterias/landing/federal')


    conteudo_site = response.headers['IBM-Web2-Location']

    url = PARTE1 + conteudo_site + PARTE2 + args + PARTE3

    response = requests.get(url)

    #print(response.content)
    byte_response = response.content

    string_json = "[" + byte_response.decode('utf8')+ "]"

    final_json = json.loads(string_json)
    for item in final_json:
        print(item['dezenasSorteadasOrdemSorteio'])
except Exception as e:
    print(e)
