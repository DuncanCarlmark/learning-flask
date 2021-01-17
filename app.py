from flask import Flask

# Page imports
import main_page

app = Flask(__name__)

@app.route('/')
def idex():
    return main_page.load_html()

if __name__ == '__main__':
    app.run(debug=True)