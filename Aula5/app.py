from flask import Flask, request, render_template_string

app = Flask(__name__)

def mostra_login():
    return render_template_string("""
    <h2>Login</h2>

    <form method="POST">
        <input type="text" name="usuario" placeholder="Usuário"><br><br>
        <input type="password" name="senha" placeholder="Senha"><br><br>

        <button type="submit">Entrar</button>
    </form>
    """)

def faz_login():
    usuarioDigitado = request.form.get('usuario')
    senha = request.form.get('senha')

    usuariosAutorizados = [
        {"nome": "janaina", "senha": "cotemig2026"},
        {"nome": "marcos", "senha": "cotemig2026"},
        {"nome": "markin", "senha": "12400688"}
    ]

    for usuario in usuariosAutorizados:
        if usuario["nome"] == usuarioDigitado and usuario["senha"] == senha:
            print("Acesso autorizado")
            return "<h1>Acesso autorizado</h1>"

    return "<h1>Login inválido</h1>"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return faz_login()
    return mostra_login()

if __name__ == '__main__':
    app.run(debug=True)