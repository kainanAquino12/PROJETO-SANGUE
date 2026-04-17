from flask import Flask, request, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def carregar_doador():
    with open('doadores.json', 'r') as f:
        return json.load(f)
    
def carregar_estoque():
    with open('estoque.json', 'r') as f:
        return json.load(f)

def carregar_sangue():
    with open('sangue.json', 'r') as f:
        return json.load(f)

def salvar(doadores):
    with open('doadores.json', 'w') as f:
        json.dump(doadores, f, indent=4)    

@app.get('/doadores/<int:id>')
def get_doadores3(id):
    doadores = carregar_doador()
    for doador in doadores:
        if doador.get("id") == id:
            return jsonify(doador), 200
    return jsonify({"error": "Doador não encontrado."}), 404



# ─────────────────────────────────────────
#  DOADORES
# ─────────────────────────────────────────

@app.post('/doadores')
def criar_doadores():
    dados = request.get_json()

    if not dados:
        return jsonify({"error": "JSON não enviado ou inválido."}), 400

    if not dados.get('paciente'):
        return jsonify({"error": "O campo 'paciente' é obrigatório."}), 400

    if not isinstance(dados.get('paciente'), str):
        return jsonify({"error": "'paciente' deve ser um texto (string)."}), 422

    if 'idade' not in dados:
        return jsonify({"error": "O campo 'idade' é obrigatório."}), 400

    if not isinstance(dados.get('idade'), int):
        return jsonify({"error": "'idade' deve ser um número inteiro."}), 422

    with open('doadores.json', 'r') as f:
        doadores = json.load(f)

    doadores.append(dados)

    with open('doadores.json', 'w') as f:
        json.dump(doadores, f, indent=4, ensure_ascii=False)

    return jsonify({"message": "Doador criado com sucesso."}), 201


@app.get('/doadores2')
def get_doadores1():
    doadores = carregar_doador()

    tipo = request.args.get('paciente')
    idade = request.args.get('idade')

    resultado = []
    for doador in doadores:
        if  tipo and doador.get('paciente') != tipo:
            continue
        if idade and doador.get('idade') != int(idade):
            continue    
        resultado.append(doador) 
    return jsonify(resultado), 200   



@app.route('/doadores', methods=['GET'])
def listar_doadores():
    with open('doadores.json', 'r') as f:
        doadores = json.load(f)

    return jsonify(doadores)


# ─────────────────────────────────────────
#  ESTOQUE
# ─────────────────────────────────────────

@app.get('/estoque/<int:id>')
def get_estoque(id):
    estoque = carregar_estoque()
    for item in estoque:
        if item.get("id") == id:
            return jsonify(item), 200
    return jsonify({"error": "Item de estoque não encontrado."}), 404



@app.post('/estoque')
def criar_estoque():
    dados = request.get_json()

    
    if 'tipo' not in dados or not dados.get('tipo'):
        return jsonify({"error": "O campo 'tipo' é obrigatório."}), 400

   
    if not isinstance(dados.get('tipo'), str):
        return jsonify({"error": "'tipo' deve ser um texto (string)."}), 422

    if 'quantidade' not in dados:
        return jsonify({"error": "O campo 'quantidade' é obrigatório."}), 400

    if not isinstance(dados.get('quantidade'), int):
        return jsonify({"error": "'quantidade' deve ser um número inteiro."}), 422

    with open('estoque.json', 'r') as f:
        estoque = json.load(f)

    estoque.append(dados)

    with open('estoque.json', 'w') as f:
        json.dump(estoque, f, indent=4, ensure_ascii=False)

    return jsonify({"message": "Estoque criado com sucesso."}), 201


@app.route('/estoque', methods=['GET'])
def listar_estoque():
    with open('estoque.json', 'r') as f:
        estoque = json.load(f)



@app.get('/estoque2')
def get_estoque2():
    estoque = carregar_estoque()

    doador = request.args.get('doador')
    vencimento = request.args.get('vencimento')

    resultado = []
    for item in estoque:
        if  doador and item.get('doador') != doador:
            continue
        if vencimento and item.get('vencimento') != str(vencimento):
            continue    
        resultado.append(item) 
    return jsonify(resultado), 200


# ─────────────────────────────────────────
#  SANGUE
# ─────────────────────────────────────────

@app.get('/sangue2')
def get_sangue2():
    sangue = carregar_sangue()

    paciente = request.args.get('paciente')
    quantidade = request.args.get('quantidade')

    resultado = []
    for item in sangue:
        if  paciente and item.get('paciente') != paciente:
            continue
        if quantidade and item.get('quantidade') != int(quantidade):
            continue    
        resultado.append(item) 
    return jsonify(resultado), 200   


@app.get('/sangue/<int:id>')
def get_sangue(id):
    sangue = carregar_sangue()
    for item in sangue:
        if item.get("id") == id:
            return jsonify(item), 200
    return jsonify({"error": "Item de sangue não encontrado."}), 404



@app.post('/sangue')
def criar_sangue():
    dados = request.get_json()

    
    if not dados.get('sangue'):
        return jsonify({"error": "O campo 'sangue' é obrigatório."}), 400

   
    if not isinstance(dados.get('sangue'), str):
        return jsonify({"error": "'sangue' deve ser um texto (string)."}), 422

    if 'quantidade' not in dados:
        return jsonify({"error": "O campo 'quantidade' é obrigatório."}), 400

    if not isinstance(dados.get('quantidade'), int):
        return jsonify({"error": "'quantidade' deve ser um número inteiro."}), 422

    
    if 'data' in dados and not isinstance(dados.get('data'), str):
        return jsonify({"error": "'data' deve ser um texto (string)."}), 422

    with open('sangue.json', 'r') as f:
        sangue = json.load(f)

    sangue.append(dados)

    with open('sangue.json', 'w') as f:
        json.dump(sangue, f, indent=4, ensure_ascii=False)

    return jsonify({"message": "Sangue criado com sucesso."}), 201


@app.route('/sangue', methods=['GET'])
def listar_sangue():
    with open('sangue.json', 'r') as f:
        sangue = json.load(f)



    return jsonify(sangue)
if __name__ == '__main__':
    app.run(debug=True)