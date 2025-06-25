from flask import Flask, request, jsonify
import utils

app = Flask(__name__)

utils.load_saved_artifacts()

@app.route('/', methods=['GET'])
def index():

    return "Welcome to the Image Classification API!"

@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    image_data = request.form['image_data']

    response = jsonify(utils.classify_image(image_data))

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
if __name__ == "__main__":
    print("Starting Flask server...")
    
    app.run()
