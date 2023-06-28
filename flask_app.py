from flask import Flask, render_template, request
import os
import openai
from time import time,sleep


app = Flask(__name__)

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

# Create an openaiapikey.txt file and save your api key.
openai.api_key = open_file('openaiapi.txt')


def bot(prompt, engine='text-davinci-003', temp=0.9, top_p=1.0, tokens=1000, freq_pen=0.0, pres_pen=0.5, stop=['<<END>>']):
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen,
        stop=[" User:", " AI:"])

    return response['choices'][0]['text'].strip()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    botresponse = bot(prompt=userText)
    return str(botresponse)

if __name__ == "__main__":
    app.run(debug=True)
