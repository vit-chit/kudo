from flask import Flask, render_template, request
import requests

app = Flask(__name__)

TOKEN = "6298888343:AAGluPIK-70yX38AkJKZft4rcqK6VhxHebs"
chat_id = "666632408"

@app.route('/join', methods=['POST', 'GET'])
def joins():
    message = 'Новая заявка с сайта\n'
    answ = ''
    if request.method == 'POST':
        message += f"Имя: {request.form['name']}\n"
        message += f"Возраст: {request.form['age']}\n"
        message += f"Телефон: {request.form['tel']}\n"
        message += f"Комментарии: {request.form['comm']}"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        # print(requests.get(url).json())
        requests.get(url)
        answ = 'Спасибо!'

        
    
    return render_template('join.html', answer = answ)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/foto', methods=['POST', 'GET'])
def foto():
    return render_template('foto.html')

@app.route('/contacts', methods=['POST', 'GET'])
def contacts():
    return render_template('contacts.html')

@app.route('/instructors', methods=['POST', 'GET'])
def instructors():
    return render_template('instructors.html')