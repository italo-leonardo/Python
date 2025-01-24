import requests
import pprint

link = "https://servicodados.ibge.gov.br/api/v3/agregados/1285/periodos/2010/variaveis/603|611|604|605?localidades=N1[all]"

requisicao = requests.get(link)
informacoes = requisicao.json()

pprint.pprint(informacoes[0])