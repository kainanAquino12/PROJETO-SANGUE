from flask import Flask, request, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ─────────────────────────────────────────
# AUXILIARES
# ─────────────────────────────────────────

def carregar_doador():
    with open('doadores.json', 'r') as f:
        return json.load(f)

def carregar_estoque():
    with open('estoque.json', 'r') as f:
        return json.load(f)

def carregar_sangue():
    with open('sangue.json', 'r') as f:
        return json.load(f)

def salvar_doadores(doadores):
    with open('doadores.json', 'w') as f:
        json.dump(doadores, f, indent=4, ensure_ascii=False)

def salvar_estoque(estoque):
    with open('estoque.json', 'w') as f:
        json.dump(estoque, f, indent=4, ensure_ascii=False)

def salvar_sangue(sangue):
    with open('sangue.json', 'w') as f:
        json.dump(sangue, f, indent=4, ensure_ascii=False)


# ─────────────────────────────────────────
# DOADORES
# ─────────────────────────────────────────

@app.get('/doadores/<int:id>')
def get_doadores3(id):
    doadores = carregar_doador()
    for doador in doadores:
        if doador.get("id") == id:
            return jsonify(doador), 200
    return jsonify({"error": "Doador não encontrado."}), 404


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

    doadores = carregar_doador()
    doadores.append(dados)
    salvar_doadores(doadores)
    return jsonify({"message": "Doador criado com sucesso."}), 201


@app.get('/doadores2')
def get_doadores1():
    doadores = carregar_doador()
    tipo = request.args.get('paciente')
    idade = request.args.get('idade')
    resultado = []
    for doador in doadores:
        if tipo and doador.get('paciente') != tipo:
            continue
        if idade and doador.get('idade') != int(idade):
            continue
        resultado.append(doador)
    return jsonify(resultado), 200


@app.route('/doadores', methods=['GET'])
def listar_doadores():
    doadores = carregar_doador()
    return jsonify(doadores)


@app.put('/doadores/<int:id>')
def atualizar_doador(id):
    doadores = carregar_doador()
    dados = request.get_json()

    if not dados:
        return jsonify({"error": "JSON não enviado ou inválido."}), 400

    for i, doador in enumerate(doadores):
        if doador.get("id") == id:
            # Atualiza os campos, mas preserva o id original
            dados['id'] = id
            doadores[i] = dados
            salvar_doadores(doadores)
            return jsonify(doadores[i]), 200

    return jsonify({"error": "Doador não encontrado."}), 404


@app.delete('/doadores/<int:id>')
def deletar_doador(id):
    doadores = carregar_doador()

    for i, doador in enumerate(doadores):
        if doador.get("id") == id:
            doadores.pop(i)
            salvar_doadores(doadores)
            return jsonify({"message": f"Doador com id {id} removido com sucesso."}), 200

    return jsonify({"error": "Doador não encontrado."}), 404


# ─────────────────────────────────────────
# ESTOQUE
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

    estoque = carregar_estoque()
    estoque.append(dados)
    salvar_estoque(estoque)
    return jsonify({"message": "Estoque criado com sucesso."}), 201


@app.route('/estoque', methods=['GET'])
def listar_estoque():
    estoque = carregar_estoque()
    return jsonify(estoque)


@app.get('/estoque2')
def get_estoque2():
    estoque = carregar_estoque()
    doador = request.args.get('doador')
    vencimento = request.args.get('vencimento')
    resultado = []
    for item in estoque:
        if doador and item.get('doador') != doador:
            continue
        if vencimento and item.get('vencimento') != str(vencimento):
            continue
        resultado.append(item)
    return jsonify(resultado), 200


@app.put('/estoque/<int:id>')
def atualizar_estoque(id):
    estoque = carregar_estoque()
    dados = request.get_json()

    if not dados:
        return jsonify({"error": "JSON não enviado ou inválido."}), 400

    for i, item in enumerate(estoque):
        if item.get("id") == id:
            # Atualiza os campos, mas preserva o id original
            dados['id'] = id
            estoque[i] = dados
            salvar_estoque(estoque)
            return jsonify(estoque[i]), 200

    return jsonify({"error": "Item de estoque não encontrado."}), 404


@app.delete('/estoque/<int:id>')
def deletar_estoque(id):
    estoque = carregar_estoque()

    for i, item in enumerate(estoque):
        if item.get("id") == id:
            estoque.pop(i)
            salvar_estoque(estoque)
            return jsonify({"message": f"Item de estoque com id {id} removido com sucesso."}), 200

    return jsonify({"error": "Item de estoque não encontrado."}), 404


# ─────────────────────────────────────────
# SANGUE
# ─────────────────────────────────────────

@app.get('/sangue2')
def get_sangue2():
    sangue = carregar_sangue()
    paciente = request.args.get('paciente')
    quantidade = request.args.get('quantidade')
    resultado = []
    for item in sangue:
        if paciente and item.get('paciente') != paciente:
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

    sangue = carregar_sangue()
    sangue.append(dados)
    salvar_sangue(sangue)
    return jsonify({"message": "Sangue criado com sucesso."}), 201


@app.route('/sangue', methods=['GET'])
def listar_sangue():
    sangue = carregar_sangue()
    return jsonify(sangue)


@app.put('/sangue/<int:id>')
def atualizar_sangue(id):
    sangue = carregar_sangue()
    dados = request.get_json()

    if not dados:
        return jsonify({"error": "JSON não enviado ou inválido."}), 400

    for i, item in enumerate(sangue):
        if item.get("id") == id:
            # Atualiza os campos, mas preserva o id original
            dados['id'] = id
            sangue[i] = dados
            salvar_sangue(sangue)
            return jsonify(sangue[i]), 200

    return jsonify({"error": "Item de sangue não encontrado."}), 404


@app.delete('/sangue/<int:id>')
def deletar_sangue(id):
    sangue = carregar_sangue()

    for i, item in enumerate(sangue):
        if item.get("id") == id:
            sangue.pop(i)
            salvar_sangue(sangue)
            return jsonify({"message": f"Item de sangue com id {id} removido com sucesso."}), 200

    return jsonify({"error": "Item de sangue não encontrado."}), 404


if __name__ == '__main__':
    app.run(debug=True)