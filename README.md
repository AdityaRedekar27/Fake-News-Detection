# 📰 Fake News Detection System (Machine Learning Project)

## 📌 Project Overview

This project is a **Fake News Detection Web Application** built using **Machine Learning and Flask**.
It classifies news as **Real 🟢 or Fake 🔴** using multiple ML algorithms.

The system allows users to:

* Enter news text manually
* Paste a news article URL
* Select different ML models
* Get prediction results instantly via a web interface

---

## 🚀 Features

* ✅ Detect Fake vs Real News
* ✅ Supports **Text Input & URL Input**
* ✅ Multiple ML Models:

  * Logistic Regression
  * Decision Tree
  * Support Vector Machine (SVM)
  * K-Nearest Neighbors (KNN)
  * Random Forest
* ✅ Clean and Interactive UI (Flask + HTML/CSS)
* ✅ Real-time Prediction
* ✅ Model Training Button

---

## Dataset
Dataset is taken from Kaggle:
https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

---

## 🛠️ Technologies Used

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python (Flask)
* **Machine Learning:** scikit-learn
* **Libraries:**

  * pandas
  * numpy
  * sklearn
  * newspaper3k (for URL content extraction)

---

## 📂 Project Structure

```
ML_Project/
│
├── app.py
├── Fake.csv
├── True.csv
├── requirements.txt
└── templates/
    └── index.html
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/fake-news-detection.git
cd fake-news-detection
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
python app.py
```

### 4️⃣ Open in Browser

```
http://127.0.0.1:5000
```

---

## 📊 How It Works

1. Load dataset (**Fake.csv + True.csv**)
2. Preprocess text (cleaning, removing special characters)
3. Convert text into numerical form using **TF-IDF Vectorizer**
4. Train multiple ML models
5. User inputs text or URL
6. Model predicts:

   * **Real News 🟢**
   * **Fake News 🔴**

---

## 🧪 Sample Inputs

### Fake News Example:

> "Scientists confirm drinking 10 cups of coffee cures cancer"

### Real News Example:

> "Government announces new economic reforms to support small businesses"

---

## 📈 Evaluation Metrics

The models are evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score

---

## ⚠️ Limitations

* Model accuracy depends on dataset quality
* URL extraction may fail for some websites
* Predictions are not 100% accurate

---

## 🔮 Future Improvements

* Add deep learning models (LSTM, BERT)
* Deploy application online (Heroku/Render)
* Add confidence score
* Improve UI/UX
* Add real-time news API integration

---

## 👨‍💻 Author

**Aditya Redekar**
B.Tech Computer Science Student

---

## ⭐ Acknowledgement

* Kaggle datasets for Fake News Detection
* scikit-learn documentation
* Flask framework

---

## 📌 Note

This project is for **educational purposes only** and should not be used as the sole source for verifying news authenticity.

---

## 🌟 If you like this project

Give it a ⭐ on GitHub!
