import pandas as pd

# Leer la base de datos de enfermedades del corazón
df = pd.read_csv("processed.cleveland_repaired.csv")

# Discretizar la edad en 3 grupos
df['age'] = pd.cut(df['age'], bins=[0, 45, 55, 100], labels=['0-45', '45-55', '55-100'])

# Discretizar la presión en 3 grupos
df['trestbps'] = pd.cut(df['trestbps'], bins=[0, 120, 140, 300], labels=['0-120', '120-140', '140-300'])

# Discretizar el colesterol en 3 grupos
df['chol'] = pd.cut(df['chol'], bins=[0, 240, 260, 400], labels=['0-240', '240-260', '260-400'])

# Discretizar el "thalach" en 3 grupos
df['thalach'] = pd.cut(df['thalach'], bins=[0, 50, 65, 202], labels=['0-50', '50-65', '65-202'])

# Discretizar el Oldpeak en 2 grupos
df['oldpeak'] = pd.cut(df['oldpeak'], bins=[0, 0.5, 6.2], labels=['0-0.5', '0.5-6.2'])

# Verificar los cambios
print(df.head())