from flask import Flask, request
# Page imports
import main_page, callback_page


app = Flask(__name__)

@app.route('/')
def idex():
    return main_page.load_html()

@app.route('/callback/')
def callback():
    code = request.args.get('code')
    return callback_page.load_html()

if __name__ == '__main__':
    app.run(debug=True)