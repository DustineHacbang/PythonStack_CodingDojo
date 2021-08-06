from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'asdfasdfadsfasd'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = int(0)
    if 'msg' not in session:
        session['msg'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
    session['building'] = request.form['building']
    if session['building'] == 'farm':
        temp = random.randint(10,20)
        session['gold'] += int(temp)
        session['msg'].append(f"Went to the farm, got {temp} gold ")  
    if session['building'] == 'cave':
        session['gold'] += random.randint(5,10)
    if session['building'] == 'house':
        session['gold'] += random.randint(2,5)
    if session['building'] == 'casino':
        session['gold'] += random.randint(-50,50)
   
   
   
   
   
    return redirect('/')

if __name__ == "__main__":
        app.run(debug=True)   