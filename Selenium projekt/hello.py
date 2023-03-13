from flask import Flask

app = Flask(__name__)

def make_blod(function):
    def dec1():
        return f"<b>{function()}</b>"
    return dec1

@app.route('/')
@make_blod
def Hello_world():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)