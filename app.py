
from api import get_major_difference_buy_ask_rate, get_max_min_average,get_average_exchange_rate


from flask import Flask, jsonify


app = Flask(__name__)

@app.route("/exchanges/<currency_code>/<date>")
def exchange_rate(currency_code, date):
    rate = get_average_exchange_rate(date, currency_code)
    return jsonify({"rate": rate})


@app.route("/exchanges/<currency_code>/maxmin/<int:num_quotes>")
def max_min_average(currency_code, num_quotes):
    max_rate, min_rate = get_max_min_average(currency_code, num_quotes)
    return jsonify({"max_rate": max_rate, "min_rate": min_rate})


@app.route("/exchanges/<currency_code>/major_difference/<int:num_quotes>")
def major_difference_buy_ask_rate(currency_code, num_quotes):
    difference = get_major_difference_buy_ask_rate(currency_code, num_quotes)
    return jsonify({"major_difference": difference})


if __name__ == "__main__":
    app.run(debug=True)
