# main.py
from flask import Flask, render_template, request, redirect, url_for
from criar_conta import criar_conta
from fazer_login import fazer_login

app = Flask(__name__)

# "Banco de dados" simples, só pra guardar a conta criada (igual antes)
nome_salvo = ''
cpf_salvo = ''
senha_salva = ''


@app.route("/", methods=["GET"])
def pagina_inicial():
    return render_template("index.html")


@app.route("/criar-conta", methods=["GET", "POST"])
def rota_criar_conta():
    global nome_salvo, cpf_salvo, senha_salva
    mensagem = None

    if request.method == "POST":
        nome = request.form.get("nome")
        idade = request.form.get("idade")
        cpf = request.form.get("cpf")
        senha = request.form.get("senha")
        confirmar_senha = request.form.get("confirmar_senha")

        resultado = criar_conta(nome, idade, cpf, senha, confirmar_senha)

        if resultado[0] is not None:
            nome_salvo, cpf_salvo, senha_salva = resultado
            mensagem = "Cadastro criado com sucesso!"
            return redirect(url_for("pagina_inicial"))
        else:
            mensagem = "Senhas não conferem."

    return render_template("criar_conta.html", mensagem=mensagem)


@app.route("/login", methods=["GET", "POST"])
def rota_login():
    resultado = None

    if request.method == "POST":
        cpf_login = request.form.get("cpf_login")
        senha_login = request.form.get("senha_login")

        resultado = fazer_login(nome_salvo, cpf_salvo, senha_salva, cpf_login, senha_login)

    return render_template("login.html", resultado=resultado, nome=nome_salvo)


if __name__ == "__main__":
    app.run(debug=True)     
    
 