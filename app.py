from flask import Flask, request, jsonify
from flask_cors import CORS
from data_predict import model_predict 

app = Flask(__name__)
CORS(app)  

@app.route('/')
def hello_word():
    return 'Hello World'

@app.route('/data', methods=['GET'])
def handle_get():
    data = {
        'Review': "This DVD will be a disappointment if you get it hoping to see some substantial portion of the acts of the various comics listed on the cover. All you get here are snippets of performance, at best. The rest is just loose-leaf reminiscence about the good old days in Boston, in the early 80's, when a lot of comics were hanging out together and getting their start. It's like a frat house reunion. There's a lot of lame nostalgia. There are quite a few guffaws recalling jokes (practical and otherwise) perpetrated - back then. But you had to have been there to appreciate all the basically good ol' boy camaraderie. If you weren't actually a part of that scene, all this joshing and jostling will fall flat. If you want to actually hear some of these comics' routines - you will have to look elsewhere.",
        'prediction': 'negative',
    }
    return jsonify(data)

@app.route('/predict', methods=['POST'])
def handle_post():
    text = request.form['review']
    prediction = model_predict(text=text)
    
    data = {
        'review' : text,
        'prediction': prediction[0],
        'polarity' : float(prediction[1][0][0])
    }
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
