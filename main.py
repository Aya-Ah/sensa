import numpy as np
import pandas as pd
import keras
import streamlit as st
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

# Tokenising training data set
tokenizer = Tokenizer(1512, lower=True, oov_token='UNK')  # num_words=1512
df_train = pd.read_csv('train.txt', header=None, sep=';', names=['Input', 'Sentiment'], encoding='utf-8')
x = df_train['Input']
tokenizer.fit_on_texts(x)

# To load the model:
from keras.models import load_model

saved_mdl = load_model("my_model")

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__, static_folder='static')


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")


@app.route('/result', methods=["POST"])
def result():
    global INPUT
    INPUT = request.form.get("txt")
    # Test your sentence
    x_ = np.array([INPUT])
    # Convert text to sequences using keras
    x_input = tokenizer.texts_to_sequences(x_)
    # Pad sequences to get uniform length
    x_input_pad = pad_sequences(x_input, maxlen=80, padding='post')

    predict_input = saved_mdl([x_input_pad])
    classes_ = np.argmax(predict_input, axis=1)
    # print(classes_x)

    categories = ['joy', 'anger', 'love', 'sadness', 'fear', 'surprise']
    global classe
    classe = categories[int(classes_)]

    if (classes_ == 0 or classes_ == 2):
        main_categories = "Positive"
    elif (classes_ == 1 or classes_ == 3):
        main_categories = "Negative"
    else:
        main_categories = "Neutral"

    return render_template("result.html", cls=classe, input=INPUT, mainc=main_categories)


if __name__ == '__main__':
    app.debug = True
    app.run()  # go to http://localhost:5000/ to view the page.


# st.stop()
raise st.script_runner.StopException
