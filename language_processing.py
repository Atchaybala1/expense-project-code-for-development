import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Re-load the correct expense data to ensure 'description' column is present
df_expenses = pd.read_csv('expense_data.csv')

# Download necessary NLTK data (if not already downloaded)
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Function to remove stop words and lemmatize
def preprocess_text(text):
    # Ensure text is string before splitting
    if not isinstance(text, str):
        return ''
    tokens = text.split()  # Simple tokenization by splitting on space
    filtered_tokens = [word for word in tokens if word not in stop_words]
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]
    return ' '.join(lemmatized_tokens)

df_expenses['description'] = df_expenses['description'].apply(preprocess_text)

print("Descriptions after removing stop words and lemmatization:")
print(df_expenses.head())
