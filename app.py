import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the model and tokenizer
model = tf.keras.models.load_model('LiveToxicComment.h5')
with open('tokenizer.pkl', 'rb') as file:
    tokenizer= pickle.load(file)

@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        sentence = request.form["sentence"]
        sequences = tokenizer.texts_to_sequences([sentence])
        padded_sequences = pad_sequences(sequences, maxlen=300, padding='post', truncating='post')
        prediction = model.predict(padded_sequences)
        if prediction[0] < 0.5:
            result = 'Bad sequence'
        else:
            result = 'Normal sequence'
        return render_template("index.html", prediction=result, input_text=sentence)
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
