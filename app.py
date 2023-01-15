from flask import Flask, render_template, request
from openaix import getLanguageTranslation
app = Flask(__name__)

app.config['SECRET_KEY'] = 'sk-pneXYherrT5X7fEDFXYoT3Bl'secret key'


@app.route('/', methods=['GET'])
def home():
    if request.method == 'POST':
        prompt = request.form['aiPrompt']
        language = request.form['aiLanguage']

        answer = getLanguageTranslation(prompt, language)

    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(host="0.0.0.0", port='8000', debug=True)
