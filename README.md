## About

I once participated in a project as a volunteer. There, I used Flask, Json, and MongoDB. this was quite helpful.

## Getting Started

1. Install the requirements:

pip install -r requirements.txt

2. Start the server:
  
python app.py

3. Test: 

python -m unittest discover -s tests

4. You can check manually differenet examples: 

curl http://localhost:5000/exchanges/USD/maxmin/5
curl http://localhost:5000/exchanges/EUR/maxmin/5
curl http://localhost:5000/exchanges/GBP/major_difference/5

