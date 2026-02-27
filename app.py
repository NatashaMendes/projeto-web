# Importa a classe Flask da biblioteca flask
# Sem essa linha, o Python não sabe o que é "Flask"
from flask import Flask, render_template

# Cria a instância da aplicação Flask
# __name__ é uma variável especial do Python que contém o nome do módulo atual
# O Flask usa isso para saber onde procurar os templates e arquivos estáticos
app = Flask(__name__)


# O decorador @app.route define qual URL aciona esta função
# '/' é a rota raiz — o endereço principal do site (ex: http://localhost:5000/)
@app.route('/')
def FeiticeiroDeClasseEspecial():
    return render_template('index.html')

# usar ''' da pra montar texto grande.
@app.route('/sobre')
def JJK():
    return render_template('sobre.html')

@app.route('/bootstrap')
def bootstrap():
    return render_template('bootstrap.html')

#variaveis. <conteudo> vai ser mudado conforme a cor que você escolhe em inglês
@app.route('/cor/<cor1>')
def exibe_cor(cor1):
    return f'<h1 style="color:{cor1}">A cor escolhida foi: {cor1}</h1>'   


@app.route('/cor/<cor1>/<cor2>')
def exibe_cor2(cor1, cor2):
    return f'<h1 style="color:{cor1}">A cor escolhida foi: {cor1} e <b style="color:{cor2}">{cor2}</b></h1>'  


@app.route('/')
def pagina_inicial():
    # Esta função retorna o que o navegador vai receber como resposta
    # Por enquanto, retornamos uma string HTML simples
    return '<h1>Olá, mundo!</h1><p>Meu primeiro servidor Flask está funcionando!!!.</p>'

@app.route('/varias-linhas')
def varias_linhas():
    return '''
    <h1>Várias Linhas</h1>
    <p> Este exemplo de resposta com várias linhas de HTML.</p>
    <ul>
      <li>Item 1</li>
      <li>Item 2</li2>
      <li>Item 3</li3>
    </ul>
    '''

# Bloco de execução: só roda quando o arquivo é executado diretamente
if __name__ == '__main__':
    # debug=True ativa o recarregamento automático ao salvar o arquivo
    # NUNCA use debug=True em produção (servidor público)
    app.run(debug=True)