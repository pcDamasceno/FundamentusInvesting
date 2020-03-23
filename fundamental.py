'''
Utiliza dados verificados no finance.yahoo.com
para analisar os indices fundamentalistas de uma empresa

INICIO 22/03/2020
'''


import time
import urllib3
import requests
from requests.exceptions import HTTPError, Timeout
from bs4 import BeautifulSoup
import pandas as pd


def fundamentusStats(stock):
    try:
        sourceCode = requests.get(
            'https://www.fundamentus.com.br/detalhes.php?papel={}'.format(stock))
    except HTTPError as http_err:
        print(f'erro HTTP: {http_err}')
    except Timeout:
        print('Timeout')
    except Exception as e:
        print('Fail ' + str(e))

    # data = sourceCode_soup.find('td', class_='data w2')

    pl = sourceCode.text.split(
        'P/L</span></td>')[1].split('txt">')[1].split('</span>')[0].replace(',', '.')

    if float(pl) < 20:
        # pl>20 -- acao cara.  #pl<3 = acao excecivamente barata
        print('{stock}:\t P/L = {pl}'.format(stock=stock, pl=pl))
    '''
    dividendYeld =
    pVp =
    vpa =
    dbPl =
    roe =
    evEbit =


    f = open('response_{}.txt'.format(stock), 'w')
    f.write(str(pl))
    f.close()
    time.sleep(2)
    '''


stocks = pd.read_csv('lista_acoes_bovespa.csv')
n_stocks = stocks.Codigo.count()
stock_code = stocks.Codigo

for i in range(n_stocks):
    fundamentusStats(stock_code[i])
    time.sleep(1)
