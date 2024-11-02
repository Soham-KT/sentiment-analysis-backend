from flask import Flask, request, jsonify
from data_predict import model_predict  # Ensure this function is correctly imported

app = Flask(__name__)

@app.route('/')
def hello_word():
    return 'Hello, World!'

@app.route('/data', methods=['GET'])
def handle_get():
    # This is the data that will be returned for a GET request
    data = {
        'Review': "This DVD will be a disappointment if you get it hoping to see some substantial portion of the acts of the various comics listed on the cover. All you get here are snippets of performance, at best. The rest is just loose-leaf reminiscence about the good old days in Boston, in the early 80's, when a lot of comics were hanging out together and getting their start. It's like a frat house reunion. There's a lot of lame nostalgia. There are quite a few guffaws recalling jokes (practical and otherwise) perpetrated - back then. But you had to have been there to appreciate all the basically good ol' boy camaraderie. If you weren't actually a part of that scene, all this joshing and jostling will fall flat. If you want to actually hear some of these comics' routines - you will have to look elsewhere.",
        'prediction': 'negative',
    }
    return jsonify(data), 200

@app.route('/predict', methods=['POST'])
def handle_post():
    data = request.get_json()  # Extract JSON data from the request
    text = data.get('review')

    if not text:
        return jsonify({'error': 'Review text is missing'}), 400

    # Make prediction using the imported model_predict function
    prediction = model_predict(text=text)

    response_data = {
        'review': text,
        'prediction': prediction
    }

    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
