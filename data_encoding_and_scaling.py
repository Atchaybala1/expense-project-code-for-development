from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

# Instantiate TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the 'description' column to get TF-IDF features (X)
X = tfidf_vectorizer.fit_transform(df_expenses['description'])

# Instantiate LabelEncoder
label_encoder = LabelEncoder()

# Fit and transform the 'category' column to get numerical labels (y)
y = label_encoder.fit_transform(df_expenses['category'])

print("Shape of TF-IDF features (X):")
print(X.shape)
print("\nShape of numerical labels (y):")
print(y.shape)
