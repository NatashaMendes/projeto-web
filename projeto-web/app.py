# Importa a classe Flask da biblioteca flask
# Sem essa linha, o Python não sabe o que é "Flask"
from flask import Flask

# Cria a instância da aplicação Flask
# __name__ é uma variável especial do Python que contém o nome do módulo atual
# O Flask usa isso para saber onde procurar os templates e arquivos estáticos
app = Flask(__name__)


# O decorador @app.route define qual URL aciona esta função
# '/' é a rota raiz — o endereço principal do site (ex: http://localhost:5000/)
@app.route('/')
def pagina_inicial():
    # Esta função retorna o que o navegador vai receber como resposta
    # Por enquanto, retornamos uma string HTML simples
    return '<h1>Olá, mundo!</h1><p>Meu primeiro servidor Flask está funcionando.</p>'


# Bloco de execução: só roda quando o arquivo é executado diretamente
if __name__ == '__main__':
    # debug=True ativa o recarregamento automático ao salvar o arquivo
    # NUNCA use debug=True em produção (servidor público)
    app.run(debug=True)

#Expandindo para três rotas: 
    from flask import Flask

app = Flask(__name__)


@app.route('/')
def pagina_inicial():
    # Rota raiz: exibida quando o usuário acessa http://localhost:5000/
    return '''
        <h1>Sistema de Gestão</h1>
        <p>Bem-vindo ao sistema.</p>
        <a href="/sobre">Sobre o sistema</a> |
        <a href="/contato">Contato</a>
    '''
    # Observe que usamos três aspas (''') para strings de múltiplas linhas em Python
    # Isso permite quebrar o HTML em várias linhas sem concatenação


@app.route('/sobre')
def sobre():
    # Rota /sobre: http://localhost:5000/sobre
    return '''
        <h1>Sobre o Sistema</h1>
        <p>Este sistema foi desenvolvido na disciplina Programação para Internet.</p>
        <a href="/">Voltar ao início</a>
    '''


@app.route('/contato')
def contato():
    # Rota /contato: http://localhost:5000/contato
    return '''
        <h1>Contato</h1>
        <p>Professor: Ronan Adriel Zenatti</p>
        <p>FATEC Jahu — Gestão da Tecnologia da Informação</p>
        <a href="/">Voltar ao início</a>
    '''


if __name__ == '__main__':
    app.run(debug=True)
