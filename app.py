from flask import Flask, render_template, request
import requests

app = Flask (__name__)

API_ENDPOINT = "https://api.thecatapi.com/v1/images/search"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    nome = request.form.get('nome', None)

    if not nome:
        return render_template('index.html', erro = "Você precisa informar um nome")
    
    response = requests.get(API_ENDPOINT)

    if response.status_code == 200:
        data = response.json()
        url_imagem = data[0]['url']
        return render_template('index.html', nome=nome, url_imagem=url_imagem)
    elif response.status_code == 400:
        return render_template('index.html', erro = "Nome inválido!")
    else:
        return render_template('index.html', erro = "Falha de API, volte mais tarde!")

if __name__ == '__main__':
    app.run(debug=True)