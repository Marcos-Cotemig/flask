from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Currículo</title>
        </head>
        <style>
            html{background-color: purple; color: white; text-align: center;}
        </style>
        <body>
            <h1>Currículo</h1>

            <h2>Informações Pessoais</h2>
            <ul>
                <li><strong>Nome:</strong> Marcos Paulo</li>  
                <li><strong>Email:</strong> 12400688@aluno.cotemig.com.br</li>
                <li><strong>Telefone:</strong> (11) 99999-9999</li>
            </ul>

            <h2>Experiência Profissional</h2>
            <ul>
                <li><strong>Empresa:</strong> Construste Brasil</li>
                <li><strong>Cargo:</strong> Suporte técnico/Desenvolvimento</li>
                <li><strong>Período:</strong> Abril de 2024 - Abril de 2025</li>
            </ul>
            <h2>Endereço</h2>
            <ul>
                <li><strong>País:</strong> Brasil</li>
                <li><strong>Estado:</strong> Minas Gerais</li>
                <li><strong>Cidade:</strong> Belo Horizonte</li>
                <li><strong>Bairro:</strong> Padre Eustaquio</li>
            </ul>
            <h2>Educação</h2>
            <ul>
                <li><strong>Escola:</strong> Marista</li>
                <li><strong>Colégio:</strong> Cotemig</li>
                <li><strong>Faculdade:</strong> Vou decidir ainda</li>
                <li><strong>Tipo de curso:</strong> Técnico em Informática</li>
            </ul>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
