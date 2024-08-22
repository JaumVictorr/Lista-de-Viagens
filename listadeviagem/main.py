from flask import Flask, request, redirect, render_template

app = Flask(__name__)

viagens = []

@app.route('/')
def index():
    return render_template('index.html', methods=['GET', 'POST'], viagens=viagens)

@app.route('/adicionar_viagem', methods=['GET', 'POST'])
def adicionar_viagem():

    if request.method == 'POST':
        nome = request.form['nome']
        local = request.form['local']
        data = request.form['data']
        codigo = len(viagens)
        viagens.append([codigo, nome, local, data])
        return redirect('/')
    else:
        return render_template('adicionar_viagem.html')

@app.route('/editar_viagem/<int:codigo>', methods=['GET', 'POST'])
def editar_viagem(codigo):

    if request.method == 'POST':
        nome = request.form['nome']
        local = request.form['local']
        data = request.form['data']
        viagens[codigo] = [codigo, nome, local, data]
        return redirect('/')
    else:
        viagem = viagens[codigo]
        return render_template('editar_viagem.html', viagem=viagem)  # Renderiza o formulário de edição

@app.route('/apagar_viagem/<int:codigo>')
def apagar_viagem(codigo):
    del viagens[codigo]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
