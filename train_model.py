import numpy as np
import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Dummy data
data = pd.DataFrame({
    'X': np.arange(1, 101),
    'Y': np.arange(1, 101) * 2  # Simple linear relationship Y = 2X
})

X = data[['X']]
y = data['Y']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Save Model
joblib.dump(model, 'model.pkl')
print("Model training complete! Model saved as model.pkl")
