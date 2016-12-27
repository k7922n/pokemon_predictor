from flask import Flask, request, render_template, send_from_directory
import similarity
app = Flask(__name__)


@app.route('/')
def api_root():
  return render_template('index.html')

@app.route('/similarity')
def api_hello():
    weight = request.args['weight']
    height = request.args['height']
    index = similarity.calculate_similarity(height, weight)

    return str(index)

@app.route('/images/<path:path>')
def send_image(path):
    return send_from_directory('images', path)

if __name__ == '__main__':
    app.run(port = 8000, host='0.0.0.0')
