from flask import Flask, render_template, request
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

app = Flask(__name__)

nltk.download('punkt')
ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

tfidf = pickle.load(open('./models/vectorizer.pkl', 'rb'))
model = pickle.load(open('./models/model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        input_msg = request.form['message']
        transformed_msg = transform_text(input_msg)
        vector_input = tfidf.transform([transformed_msg])
        result = model.predict(vector_input)[0]

        if result == 1:
            prediction = "Spam"
        else:
            prediction = "Not Spam"

        return prediction

if __name__ == '__main__':
    app.run(debug=True)
