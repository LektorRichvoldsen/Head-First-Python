from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def entry_page() -> str:
    return "Hei Anders!"


if __name__ == '__main__':
    app.run(host='192.168.0.162', debug=False, port=5000)
