from flask import Flask, jsonify
import requests

app = Flask(__name__)

NBP_API_BASE = "http://api.nbp.pl/api"


def get_average_exchange_rate(date, currency_code):
    response = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/A/{currency_code}/{date}/")
    data = response.json()
    return data["rates"][0]["mid"]


def get_max_min_average(currency_code, num_quotes):
    response = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/A/{currency_code}/last/{num_quotes}/")
    data = response.json()
    rates = [rate["mid"] for rate in data["rates"]]
    return max(rates), min(rates)


def get_major_difference_buy_ask_rate(currency_code, num_quotes):
    response = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/C/{currency_code}/last/{num_quotes}/")
    data = response.json()
    differences = [rate["ask"] - rate["bid"] for rate in data["rates"]]
    return max(differences)