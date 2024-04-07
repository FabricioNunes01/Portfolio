import pandas as pd
import sweetviz as sv

# Carregar o DataFrame
df = pd.read_excel('meu_dataframe.xlsx')
df_drake = df.loc[df[1] == 'Drake'].iloc[[0]]
df = df.loc[df[1] != 'Drake']
df = pd.concat([df_drake,df])
df.columns = df.iloc[0]
df = df.drop(0)
df['Resultado'] = df['Resultado'].replace({'WIN': 1, 'LOSS': 0})
df = df.drop('Double kills', axis=1)
df = df.drop('Triple kills', axis=1)
df = df.drop('Quadra kills', axis=1)
df = df.drop('Penta kills', axis=1)
df = df.drop('Objectives Stolen', axis=1)
df = df.drop("['56817']", axis=1)
df = df.drop("CS in Enemy Jungle", axis=1)
#df = df.drop("Solo Kills", axis=1)
#df = df.drop("nan", axis=1)
df['Solo kills'] = df['Solo kills'].fillna(0, inplace=True)
df = df.dropna(axis=1)
for coluna in df.columns:
    df[coluna] = pd.to_numeric(df[coluna], errors='ignore')

from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error

# Carregue os dados
data = df

data = pd.get_dummies(data)
# Divida os dados em features (X) e target (y)

X = data.drop(columns=['Resultado'])
X.columns = X.columns.astype(str)
y = data['Resultado']

# Divida os dados em conjunto de treinamento e conjunto de teste
X, y = make_regression(n_samples=1000, n_features=10, noise=0.1, random_state=49)

# Dividir os dados em conjunto de treinamento e conjunto de teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=49)

# Inicializar os modelos
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=49),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=49),
    "Gradient Boosting": GradientBoostingRegressor(n_estimators=100, random_state=49)
}

# Treinar e avaliar cada modelo
results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    results[name] = mse

# Imprimir resultados
for name, mse in results.items():
    print(f"{name}: Mean Squared Error = {mse}")