from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def prompt():
    return render_template('form_prompt.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
       
      city = str(request.form['cityname'])
      url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=d8c155b6234b83e3ca5d68e3e5a6deed"
      response = requests.get(url)
      data = response.text
      weather_data = json.loads(data)

      
      state = str(request.form['state'])
      url = "https://api.schooldigger.com/v1.2/rankings/schools/"+state+"?appID=f14c813a&appKey=560e6e0400648906909977e5c7ff3a43"
      response = request.get(url)
      data = response.text
      school_data = json.loads(data)
      
      return render_template('form_submission.html')
        
if __name__ == '__main__':
    app.run(debug = True)
