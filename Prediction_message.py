import streamlit as st
import pickle
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# تحميل ال Model, TF-IDF, LabelEncoder باستخدام Pickle  
with open('D:\documents\DEPI (AI)\My Projects\Progress\Spam or Ham SMS Classifier/Model/model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('D:\documents\DEPI (AI)\My Projects\Progress\Spam or Ham SMS Classifier/Model/tfidf.pkl', 'rb') as file:
    tfidf = pickle.load(file)

with open('D:\documents\DEPI (AI)\My Projects\Progress\Spam or Ham SMS Classifier/Model/label_encoder.pkl', 'rb') as file:
    encoder = pickle.load(file)

# تصميم داله تقوم ب تنظيف النص المدخل
def preprocess(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower()
    words = word_tokenize(text)
    words = [out for out in words if out not in set(stopwords.words('english'))]
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word, pos= 'v') for word in words]
    clean_text = ' '.join(words)
    return clean_text

st.title('Welcome to Spam/Ham Classifier. \nV 0.0.1')
user_text = st.text_area('Enter your message here: ') #طلب النص من العميل 

if st.button('Classify'):
    if user_text.strip() == '':
        st.warning('Please enter your message')
    else:
        # معالجه الداتا و استخدام المودل للتنبأ
        Clean_text = preprocess(user_text)
        vector_text = tfidf.transform([Clean_text]).toarray()
        prediction = model.predict(vector_text)
        encode_prediction = encoder.inverse_transform(prediction)

        st.subheader(f'This message is:')
        st.info(encode_prediction[0])
