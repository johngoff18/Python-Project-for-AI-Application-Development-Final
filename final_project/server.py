from machinetranslation import translator
from flask import Flask, render_template, request
import json

#create module to handle translation

app = Flask(__name__)

# create route for english to french
@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translation = translator.englishToFrench(textToTranslate)
    return json.dumps(translation)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translation = translator.frenchToEnglish(textToTranslate)
    return json.dumps(translation)



@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
