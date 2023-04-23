## About my experience

I've done a project before as a volunteer. I used Flask there, putting it up and deploying it to Docker. This was very useful.

I researched on this project: Swagger, unittest library, JSON

Useful link: https://api.nbp.pl/en.html#data_sources

## Getting Started

1. Install the requirements:

pip install -r requirements.txt

2. Start the server:
  
python app.py

3. Test: 

python -m unittest discover -s tests

4. You can check manually differenet examples: 

curl http://localhost:5000/exchanges/USD/2023-01-02

curl http://localhost:5000/exchanges/EUR/maxmin/5

curl http://localhost:5000/exchanges/GBP/major_difference/5

