import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Load the dataset
df = pd.read_csv('dataset.csv')


# Convert 'lastUpdated' to datetime and extract features
def extract_date_time_features(df):
    df['lastUpdated'] = pd.to_datetime(df['lastUpdated'])
    df['hour'] = df['lastUpdated'].dt.hour
    df['weekday'] = df['lastUpdated'].dt.weekday
    return df.drop('lastUpdated', axis=1)


# Apply the date time feature extraction
df = extract_date_time_features(df)

# Define which columns should be encoded vs scaled
columns_to_encode = ['systemCodeNumber', 'hour', 'weekday']  # Add categorical columns here
columns_to_scale = ['capacity']  # Add numerical columns here

# Define the transformations for numerical and categorical columns
numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),  # Impute missing values with mean
    ('scaler', StandardScaler())])  # Then scale numerical features

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='MISSING')),  # Impute missing values with 'MISSING'
    ('onehot', OneHotEncoder(handle_unknown='ignore'))])  # Then one-hot encode categorical features

# Bundle preprocessing for numerical and categorical data
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, columns_to_scale),
        ('cat', categorical_transformer, columns_to_encode)
    ])

# Split data into features and target
X = df.drop('occupancy', axis=1)  # drop the target column to create the features DataFrame
y = df['occupancy']  # create the target series

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Fit the preprocessor to the train data
preprocessor.fit(X_train)

# Save the preprocessor and the feature names for later use in prediction
joblib.dump(preprocessor, 'preprocessor.joblib')

# Transform the training and test data
X_train_processed = preprocessor.transform(X_train)
X_test_processed = preprocessor.transform(X_test)

# Check if the processed data is a sparse matrix and convert it to a dense format if it is
if hasattr(X_train_processed, "toarray"):
    X_train_processed = X_train_processed.toarray()
if hasattr(X_test_processed, "toarray"):
    X_test_processed = X_test_processed.toarray()

# Get feature names for categorical attributes
cat_features = preprocessor.named_transformers_['cat'].get_feature_names_out(input_features=columns_to_encode)
# Combine with numerical attribute names
feature_names = list(cat_features) + columns_to_scale

# Save the feature names for later use
joblib.dump(feature_names, 'feature_names.joblib')

# Now, create the DataFrames using the processed data
train_preprocessed = pd.DataFrame(X_train_processed, columns=feature_names)
train_preprocessed['occupancy'] = y_train.reset_index(drop=True)  # add the target variable

test_preprocessed = pd.DataFrame(X_test_processed, columns=feature_names)
test_preprocessed['occupancy'] = y_test.reset_index(drop=True)  # add the target variable

# Save to CSV
train_preprocessed.to_csv('train_preprocessed.csv', index=False)
test_preprocessed.to_csv('test_preprocessed.csv', index=False)
