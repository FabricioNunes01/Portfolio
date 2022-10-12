import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import openpyxl
from xlsxwriter import Workbook
import datetime




def sp(spread):

    vig = 2   
    today = datetime.datetime.now()
    x = today.strftime('%d-%m-%Y')
    dia,mes,ano = x.split("-")
    dia = int(dia) - int(vig)
    if int(dia) < 10:
        dia = str('0')+str(dia)
    if (mes) == 1:
        mes = 'jan'
    elif (mes) == 2:
        mes = 'fev'
    elif (mes) == 3:
        mes = 'mar'
    elif (mes) == 4:
        mes = 'abr'
    elif (mes) == 5:
        mes = 'mai'
    elif (mes) == 6:
        mes = 'jun'
    elif (mes) == 7:
        mes = 'jul'
    elif (mes) == 8:
        mes = 'ago'
    elif (mes) == 9:
        mes = 'set'
    elif (mes) == 10:
        mes = 'out'
    elif (mes) == 11:
        mes = 'nov'
    elif (mes) == 12:
        mes = 'dez'
        


    anbima = 'https://www.anbima.com.br/informacoes/merc-sec-debentures/resultados/mdeb_'+str(dia)+mes+str(ano)+spread+'.asp'
    pagina = urllib.request.urlopen(anbima)
    soup = BeautifulSoup(pagina, 'html5lib')
    all_table = soup.find_all('table')
    table = soup.find('table', {'cellspacing':'0'})
            
    A=[]
    B=[]
    C=[]
    D=[]
    E=[]
    F=[]
    G=[]
    H=[]
    I=[]
    J=[]
    K=[]
    L=[]
    M=[]
    N=[]
    for row in table.findAll("tr"): 
        cells = row.findAll("td") 
        if len(cells)==14: 
            A.append(cells[0].find(text=True)) 
            B.append(cells[1].find(text=True))
            C.append(cells[2].find(text=True))
            D.append(cells[3].find(text=True))
            E.append(cells[4].find(text=True))
            F.append(cells[5].find(text=True))
            G.append(cells[6].find(text=True))
            H.append(cells[7].find(text=True))
            I.append(cells[8].find(text=True))
            J.append(cells[9].find(text=True))
            K.append(cells[10].find(text=True))
            L.append(cells[11].find(text=True))
            M.append(cells[12].find(text=True))
            N.append(cells[13].find(text=True))
        
    df = pd.DataFrame(index=[], columns=[''])
            
    df['Código']=A
    df['Nome']=B
    df['Repac./ Venc.']=C
    df['Índice/ Correção']=D
    df['Taxa de Compra']=E
    df['Taxa de Venda']=F
    df['Taxa Indicativa']=G
    df['Desvio Padrão']=H
    df['Intervalo Indicativo min']=I
    df['Intervalo Indicativo max']=J
    df['PU']=K
    df['% PU Par']=L
    df['Duration']=M
    df['% Reune']=N

            
    NomeDoArquivo = 'tabelaanbima3.xlsx'
    print(anbima)
  

    df.to_excel(NomeDoArquivo, index=False)
    print('DataFrame foi escrito no Excel com sucesso.')

def ip(ipca):
    vig = 2   
    today = datetime.datetime.now()
    x = today.strftime('%d-%m-%Y')
    dia,mes,ano = x.split("-")
    dia = int(dia) - int(vig)
    if int(dia) < 10:
        dia = str('0')+str(dia)
    if (mes) == 1:
        mes = 'jan'
    elif (mes) == 2:
        mes = 'fev'
    elif (mes) == 3:
        mes = 'mar'
    elif (mes) == 4:
        mes = 'abr'
    elif (mes) == 5:
        mes = 'mai'
    elif (mes) == 6:
        mes = 'jun'
    elif (mes) == 7:
        mes = 'jul'
    elif (mes) == 8:
        mes = 'ago'
    elif (mes) == 9:
        mes = 'set'
    elif (mes) == 10:
        mes = 'out'
    elif (mes) == 11:
        mes = 'nov'
    elif (mes) == 12:
        mes = 'dez'
    anbima = 'https://www.anbima.com.br/informacoes/merc-sec-debentures/resultados/mdeb_'+dia+mes+ano+'_ipca_spread.asp'
    pagina = urllib.request.urlopen(anbima)
    soup = BeautifulSoup(pagina, 'html5lib')
    all_table = soup.find_all('table')
    table = soup.find('table', {'cellspacing':'0'})
    A=[]
    B=[]
    C=[]
    D=[]
    E=[]
    F=[]
    G=[]
    H=[]
    I=[]
    J=[]
    K=[]
    L=[]
    M=[]
    N=[]
    O=[]
    for row in table.findAll("tr"): 
        cells = row.findAll("td") 
        if len(cells)==15: 
            A.append(cells[0].find(text=True)) 
            B.append(cells[1].find(text=True))
            C.append(cells[2].find(text=True))
            D.append(cells[3].find(text=True))
            E.append(cells[4].find(text=True))
            F.append(cells[5].find(text=True))
            G.append(cells[6].find(text=True))
            H.append(cells[7].find(text=True))
            I.append(cells[8].find(text=True))
            J.append(cells[9].find(text=True))
            K.append(cells[10].find(text=True))
            L.append(cells[11].find(text=True))
            M.append(cells[12].find(text=True))
            N.append(cells[13].find(text=True))
            O.append(cells[14].find(text=True))
              


    df = pd.DataFrame(index=[], columns=[''])

    df['Código']=A
    df['Nome']=B
    df['Repac./ Venc.']=C
    df['Índice/ Correção']=D
    df['Taxa de Compra']=E
    df['Taxa de Venda']=F
    df['Taxa Indicativa']=G
    df['Desvio Padrão']=H
    df['Intervalo Indicativo min']=I
    df['Intervalo Indicativo max']=J
    df['PU']=K
    df['% PU Par']=L
    df['Duration']=M
    df['% Reune']=N
    df['Referência NTN-B']=O





    NomeDoArquivo = 'tabelaanbima2.xlsx'
  

    df.to_excel(NomeDoArquivo, index=False)
    print('DataFrame foi escrito no Excel com sucesso.')