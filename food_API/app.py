#make a POST request
import requests
#handle a POST request
from flask import Flask, redirect, render_template, request, url_for, jsonify
import socket, time
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/submit', methods=['POST'])
def my_test_endpoint():
    
    myApiKey = "13644d463db540d1ab59ec960c9c64fd"
    apiEndpoint = "https://api.spoonacular.com/food/detect"

    session = requests.Session()
    session.headers = {"Application": "spoonacular",
                       "Content-Type": "application/x-www-form-urlencoded"}
    
    response = session.request('post', apiEndpoint,
                                            timeout=5,
                                            data={"text": request.form['text']},
                                            params={'apiKey':myApiKey})
                        
    dictFromServer = response.json()
    img_url = dictFromServer['annotations'][0]['image']
    
    return redirect(img_url, code=302)

if __name__ == '__main__':
    app.run(debug=True)