#About

I once participated in a project as a volunteer. There, I used Flask, Json, and MongoDB. this was quite helpful.

## Getting Started

1. Install the requirements:

pip install -r requirements.txt

2. Start the server:
  
python app.py

3. Examples:

- To get the average exchange rate for USD on 2023-01-02:

curl http://localhost:5000/exchanges/USD/2023-01-02


- To get the max and min average value for USD in the last 5 days:

curl http://localhost:5000/exchanges/USD/maxmin/5

- To get the major difference between the buy and ask rate for USD in the last 5 days:

curl http://localhost:5000/exchanges/USD/major_difference/5

