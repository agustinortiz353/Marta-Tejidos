from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    links = [
        {"name": "Instagram", "url": "https://www.instagram.com/martatejidos_/"},
        {"name": "WhatsApp", "url": "https://wa.me/5493794049376"},
    ]
    return render_template("index.html", links=links)

if __name__ == "__main__":
    app.run(debug=True)
