# Spam Ham SMS Classifier 📩

This project is a machine learning model that classifies SMS messages as *Spam* or *Ham (Not Spam)*.  
It includes data exploration, model training, evaluation, and a Streamlit app for easy interaction.

## 🔍 About the Project

- Explored the relationship between characters, words, and sentences using a *pairplot*.
- Visualized the class distribution (*Spam vs Ham) using a **countplot*.
- Compared multiple models using a *heatmap* visualization.
- Preprocessed text data (cleaning, lowercasing, tokenization, stopword removal, lemmatization).
- Trained and compared four models: *Naive Bayes, **Random Forest, **SVC, **KNN*.
- Selected *Random Forest* as the final model due to its slightly better performance and faster training.
- Saved models and vectorizers using *Pickle* for quick reuse.
- Built a *Streamlit* app for easy user interaction.

## 📊 Model Performance

| Model         | Precision | Recall  | F1-Score | Test Accuracy |
|---------------|-----------|---------|----------|---------------|
| SVC           | 0.9921    | 0.8333  | 0.9058   | 0.9767        |
| Random Forest | 1.0000    | 0.8267  | 0.9051   | 0.9767        |
| KNN           | 1.0000    | 0.4000  | 0.5714   | 0.9193        |
| Naive Bayes   | 0.9910    | 0.7333  | 0.8429   | 0.9632        |

## 🖼 Visualizations

All visualizations are saved in the Images/ folder:

- Pairplot of Characters, Words, and Sentences
- Countplot of Spam vs Ham Classes
- Model Comparison Heatmap

## 📁 Project Structure

Spam_Ham_Classifier/
├── Images/
│   ├── Count Plot of Classes.png
│   ├── pairplot_char_word_sent.png
│   └── model_comparison_heatmap_ranked.png
├── Model/
│   ├── model.pkl
│   ├── tfidf.pkl
│   └── label_encoder.pkl
├── Notebooks/
│   └── Spam_Ham_Classifier.ipynb
├── Prediction_message.py
├── requirements.txt
├── README.md



## 📦 Requirements

Install the required libraries using:

bash
pip install -r requirements.txt





---

## 🚀 How to Run

Clone the repository:

bash
git clone https://github.com/your-username/Spam_Ham_Classifier.git
cd Spam_Ham_Classifier


Install the requirements:

bash
pip install -r requirements.txt


Run the Streamlit app:

bash
streamlit run Prediction_message.py

---

## 📩 About the Author
Built with passion and learning.
A small step towards mastering machine learning and building practical AI applications. 🚀\
Adel Mahmoud
