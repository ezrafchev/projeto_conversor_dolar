from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        amount = float(request.form["amount"])
        response = requests.get("https://open.er-api.com/v6/latest/USD")
        exchange_rate = response.json()["rates"]["BRL"]
        converted_amount = round(amount * exchange_rate, 2)
        return render_template("index.html", amount=amount, converted_amount=converted_amount, exchange_rate=exchange_rate)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
