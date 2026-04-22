from flask import Flask, render_template, request, jsonify
import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from newspaper import Article

app = Flask(__name__)

# Global variables
models = {}
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)

def clean_text(text):
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = text.lower()
    return text

def load_data():
    fake = pd.read_csv("Fake.csv")
    true = pd.read_csv("True.csv")

    fake['label'] = 0
    true['label'] = 1

    df = pd.concat([fake, true]).sample(frac=1).reset_index(drop=True)
    df = df[['text', 'label']]
    
    # Use only first 5000 rows for faster training
    df = df.head(5000)

    df['text'] = df['text'].apply(clean_text)

    return df

def train_models():
    global models, vectorizer

    df = load_data()

    X = vectorizer.fit_transform(df['text'])
    y = df['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Use only fast models instead of 5 slow ones
    models['Logistic Regression'] = LogisticRegression(max_iter=1000)
    models['Decision Tree'] = DecisionTreeClassifier(max_depth=10)
    models['Random Forest'] = RandomForestClassifier(n_estimators=50, max_depth=10)

    for name in models:
        models[name].fit(X_train, y_train)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/train', methods=['POST'])
def train():
    train_models()
    return jsonify({"message": "Model Trained Successfully!"})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        text = data.get('text', '')
        model_name = data.get('model')

        if not text:
            return jsonify({"result": "Please enter text"})
        
        if not models:
            return jsonify({"result": "❌ Please train the model first by clicking 'Train Model'"})
        
        if model_name not in models:
            return jsonify({"result": "❌ Model not found. Please select a valid model."})

        text = clean_text(text)
        vector = vectorizer.transform([text])

        prediction = models[model_name].predict(vector)[0]

        return jsonify({
            "result": "Real News 🟢" if prediction == 1 else "Fake News 🔴"
        })
    except Exception as e:
        print(f"Error in predict: {str(e)}")
        return jsonify({"result": f"❌ Error: {str(e)}"})

@app.route('/predict_url', methods=['POST'])
def predict_url():
    try:
        data = request.json
        url = data.get('url')
        model_name = data.get('model')

        if not models:
            return jsonify({"result": "❌ Please train the model first by clicking 'Train Model'"})

        article = Article(url)
        article.download()
        article.parse()

        text = clean_text(article.text)
        vector = vectorizer.transform([text])

        prediction = models[model_name].predict(vector)[0]

        return jsonify({
            "result": "Real News 🟢" if prediction == 1 else "Fake News 🔴"
        })

    except Exception as e:
        print(f"Error in predict_url: {str(e)}")
        return jsonify({"result": f"❌ Invalid URL or Error: {str(e)}"})

import webbrowser   # 👈 you can also place this at the top, both are fine

if __name__ == "__main__":
    print("Starting Fake News Detection App...")

    webbrowser.open("http://127.0.0.1:5000")  # auto open browser

    app.run(debug=True)