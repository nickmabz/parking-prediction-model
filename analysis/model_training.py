from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import joblib

# Load preprocessed data
X_train = pd.read_csv('train_preprocessed.csv')
X_test = pd.read_csv('test_preprocessed.csv')
y_train = X_train.pop('occupancy')
y_test = X_test.pop('occupancy')

# Initialize the model
model = RandomForestRegressor(n_estimators=100, random_state=0)

# Train the model
model.fit(X_train, y_train)

# Save the model for later use in prediction
joblib.dump(model, 'parking_prediction_model.joblib')

# Now you can use model to predict and evaluate your model
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# Evaluate the model
mse_train = mean_squared_error(y_train, y_train_pred)
r2_train = r2_score(y_train, y_train_pred)
mse_test = mean_squared_error(y_test, y_test_pred)
r2_test = r2_score(y_test, y_test_pred)

print(f"Training Set Mean Squared Error: {mse_train}")
print(f"Training Set R^2 Score: {r2_train}")
print(f"Test Set Mean Squared Error: {mse_test}")
print(f"Test Set R^2 Score: {r2_test}")
