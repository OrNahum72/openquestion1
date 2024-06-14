from flask import Flask, jsonify
import requests as r

app = Flask('Chuck is the best')

@app.route('/')
def jokeresponse():
    api_data = r.get('https://api.chucknorris.io/jokes/random')
    joke_json = api_data.json()
    joke = joke_json.get("value")
    return f"Your daily chuck joke is: {joke}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
