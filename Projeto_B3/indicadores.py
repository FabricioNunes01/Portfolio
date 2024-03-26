import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Baixar dados históricos da PETR4.SA
ticker = "PETR4.SA"
petrobras = yf.Ticker(ticker)
historical_data = petrobras.history(period="max")

# Baixar dados de dividendos
dividends = petrobras.dividends

# Plotar gráfico de preço de fechamento ao longo do tempo
plt.figure(figsize=(12, 6))
historical_data['Close'].plot(label='Preço de Fechamento')
plt.title(f'Histórico de Preço de Fechamento da {ticker}')
plt.xlabel('Data')
plt.ylabel('Preço de Fechamento (R$)')
plt.legend()
plt.show()

# Plotar gráfico de dividendos ao longo do tempo
plt.figure(figsize=(12, 6))
dividends.plot(kind='bar', color='green', alpha=0.7, label='Dividendos')
plt.title(f'Dividendos da {ticker}')
plt.xlabel('Data')
plt.ylabel('Valor do Dividendo (R$)')
plt.legend()
plt.show()

# Calcular o total de dividendos pagos
total_dividends = dividends.sum()
print(f"Total de dividendos pagos pela {ticker}: R$ {total_dividends:.2f}")
