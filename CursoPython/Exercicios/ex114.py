import requests

def testar_acesso(site):
    try:
        response = requests.get(site)
        if response.status_code == 200:
            print(f'Tudo ok - O site {site} está acessível.')
        else:
            print(f'Erro - O site {site} retornou o status code {response.status_code}.')
    except requests.exceptions.RequestException as e:
        print(f'Deu erro - Não foi possível acessar o site {site}. Erro: {e}')

# Exemplo de uso
testar_acesso('https://www.pudim.com.br')

