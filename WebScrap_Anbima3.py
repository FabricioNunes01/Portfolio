import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import openpyxl
from xlsxwriter import Workbook



dia = (input('Digite o dia: '))
mes = int(input('Digite o mês: '))
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


ano = input('Digite o ano: ')


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





NomeDoArquivo = 'tabelaanbima.xlsx'
  

df.to_excel(NomeDoArquivo, index=False)
print('DataFrame foi escrito no Excel com sucesso.')


#ESSA PARTE NÃO ESTÁ DANDO CERTO
writer = pd.ExcelWriter("tabelaanbima.xlsx", engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1',index=False)


workbook  = writer.book
worksheet = writer.sheets['Sheet1']


formato1 = workbook.add_format({'num_format': '#,##0.00'}) #essa é para ajustar os valores e colocar %
formato2 = workbook.add_format({'num_format': '0,00%'})

worksheet.set_column('C:C',50, formato1)
worksheet.set_column('L:L',20, formato1)
worksheet.set_column('D:D',15, formato2)
worksheet.set_column('E:E',15, formato1)
worksheet.set_column('I:I',None, formato1)
worksheet.set_column('I:I',None, formato1)

writer.save()




z = input ('Deseja mais uma planilha? ')
if z == ('sim'):
     
     dia=int(dia)
     valor = input ('Digite o valor d + x : ')
     if valor == ('d+1'):
          dia = dia + 1
     elif valor == ('d+2'):
         dia = dia + 2
     elif valor == ('d+3'):
         dia = dia + 3
     elif valor == ('d-1'):
         dia = dia - 1
     elif valor == ('d-2'):
         dia = dia - 2
     elif valor == ('d-3'):
         dia = dia - 3
     elif valor == ('d-4'):
         dia = dia - 4
     elif valor == ('d-5'):
         dia = dia - 5
     elif valor == ('d+4'):
         dia = dia + 4
     elif valor == ('d+5'):
         dia = dia + 5

     if (mes) == 1:
          mes = 'jan'
          if (dia) > 31:
              mes = 'fev'
              dia = dia - 31

     elif (mes) == 2:
         mes = 'fev'
         if (dia) > 28:
              mes = 'mar'
              dia = dia - 28
     elif (mes) == 3:
         mes = 'mar'
         if (dia) > 31:
              mes = 'abr'
              dia = dia - 31
     elif (mes) == 4:
         mes = 'abr'
         if (dia) > 30:
              mes = 'mai'
              dia = dia - 30
     elif (mes) == 5:
         mes = 'mai'
         if (dia) > 31:
              mes = 'jun'
              dia = dia - 31
     elif (mes) == 6:
         mes = 'jun'
         if (dia) > 30:
              mes = 'jul'
              dia = dia - 30
     elif (mes) == 7:
         mes = 'jul'
         if (dia) > 31:
              mes = 'ago'
              dia = dia - 31
     elif (mes) == 8:
         mes = 'ago'
         if (dia) > 31:
              mes = 'set'
              dia = dia - 31
     elif (mes) == 9:
         mes = 'set'
         if (dia) > 30:
              mes = 'out'
              dia = dia - 30
     elif (mes) == 10:
         mes = 'out'
         if (dia) > 31:
              mes = 'nov'
              dia = dia - 31
     elif (mes) == 11:
         mes = 'nov'
         if (dia) > 30:
              mes = 'dez'
              dia = dia - 30
     elif (mes) == 12:
         mes = 'dez'
         if (dia) > 31:
              mes = 'jan'
              dia = dia - 31
     dia = str(dia)



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

else:
     print('o programa se encerra aqui então')