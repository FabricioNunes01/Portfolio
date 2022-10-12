from multiprocessing import sharedctypes
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn



#aqui coloca o nome dos ativos, data de começo e fim
ativos = yf.download(tickers=['ELET3.SA','VALE3.SA'],start='2017-06-15',end='2022-06-15')['Close']
ativos = ativos.dropna()
#plt.plot(ativos)  #exemplos de como colocar o grafico
#plt.show()


# Tamanho das colunas (número de ativos)
n = len(ativos.columns)
 
# Calcula os retornos
returns = ativos/ativos.shift(1)-1
returns = returns.dropna()


#variancia
vari = returns.var()

#beta
#varbeta = returns2.var()*264
#print(varbeta)
#cov2 = returns.cov()
#beta = cov2/varbeta
#print(beta)


#maximo
maximo = returns.max()

#minimo
minimo = returns.min()

#media
retorno = returns.mean()*264
print('Esse é o retorno anual:',retorno)


#covariancia
cov = returns.cov()*264
print('Covariancia: ',cov)

#correlacao
correl = returns.corr()
print('Correlação: ',correl)

#numero de carteiras
num_cart = 1000

#peso dos ativos
peso = np.random.random(n)
peso /= np.sum(peso)

#formula retorno esperado
ret_esperado = np.dot(peso,retorno)

#formula desvio padrao
volat = np.sqrt(np.dot(peso.T,np.dot(cov,peso)))


sharpe = retorno/volat


dc_carteira = {'Retorno':ret_esperado,'Volatilidade':volat,'Sharpe':sharpe}


#lista para receber os valores com pesos diferentes
lista_p = []
lista_v = []
lista_r = []
lista_s = []
portfolio = pd.DataFrame(dc_carteira)


#comando de for para pegar todos os valores e jogar nas listas
for carteira in range(num_cart):
    peso = np.random.random(n)
    peso /= np.sum(peso)
    lista_p.append(peso)
    retorno_esperado = np.dot(peso,retorno)
    lista_r.append(retorno_esperado)
    volat = np.sqrt(np.dot(peso.T,np.dot(cov,peso)))
    lista_v.append(volat)
    sharpe = retorno_esperado/volat
    lista_s.append(sharpe)

#passar para o pandas
dc_carteira = {'Retorno':lista_r,'Volatilidade':lista_v,'Sharpe':lista_s}
portfolios = pd.DataFrame(dc_carteira)

maior_sharpe = portfolios['Sharpe'].max()
menor_sharpe = portfolios['Sharpe'].min()
carteira_maior_sharpe = portfolios.loc[portfolios['Sharpe'] == maior_sharpe]
print('maior sharpe:',carteira_maior_sharpe)
print(menor_sharpe)

#utiliza o matplot para gerar o gráfico
plt.style.use('seaborn-dark')
plt.scatter(portfolios['Volatilidade'],portfolios['Retorno'],marker='.')
plt.xlabel('Risco')
plt.ylabel('Retorno')
plt.scatter(carteira_maior_sharpe['Volatilidade'],carteira_maior_sharpe['Retorno'],marker=',',color='g')
#plt.scatter(0,0.064,marker=',',color='b')
plt.show()