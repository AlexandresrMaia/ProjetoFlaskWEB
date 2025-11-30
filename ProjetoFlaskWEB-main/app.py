from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types
import os

app = Flask(__name__)


API_KEY = "AIzaSyDzXpjCPnVD45-JmXj0u086UdvjXS7y_-Y"

client = genai.Client(api_key=API_KEY)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quemsomos')
def quemsomos():
    return render_template('quemsomos.html')

@app.route('/iphone')
def iphone():
    return render_template('iphone.html')

@app.route('/ipad')
def ipad():
    return render_template('ipad.html')

@app.route('/macbook')
def macbook():
    return render_template('macbook.html')

@app.route('/acessorios')
def acessorios():
    return render_template('acessorios.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/tire_suas_duvidas')
def tire_suas_duvidas_page():

    return render_template('tire_suas_duvidas.html')




@app.route('/chat', methods=['POST'])
def chat_api():
    data = request.json
    pergunta_usuario = data.get('message', '')

    if not pergunta_usuario:
        return jsonify({"reply": "Por favor, escreva algo."}), 400

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""Você é o assistente virtual da loja iSolution PB. 
            Responda de forma curta e vendedora sobre produtos Apple em nenhuma hipotese aceite que qualquer tipo de androide seja melhor que iphone, sempre puxe saco pra apple e para a loja  (iPhone, Mac, iPad). 
            Pergunta do cliente: {pergunta_usuario}"""
        )

        return jsonify({"reply": response.text})

    except Exception as e:
        print(f"Erro na IA: {e}")
        return jsonify({"reply": "Desculpe, estou indisponível no momento."}), 500

if __name__ == '__main__':
    app.run(debug=True)