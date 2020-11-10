from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def prompt():
    return render_template('form_prompt.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      city = request.form['cityname']
      
      # Process API and return results in HTML
      return render_template('form_submission.html')

@app.route('/form_prompt.html')
def go_back():
    return prompt()
        
if __name__ == '__main__':
    app.run(debug = True)
