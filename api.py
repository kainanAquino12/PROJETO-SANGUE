from flask import Flask, json,request, jsonify

app = Flask(__name__)
@app.post('/doadores')
def criar_doadores():
    dados = request.get_json()

    if not dados.get('paciente'):
        return jsonify({"error": "O campo 'paciente' é obrigatório."}), 400
        

    with open ('doadores.json', 'r') as f:
        doadores = json.load(f)
    doadores.append(dados)

    with open ('doadores.json', 'w') as f:
        json.dump(doadores, f, indent=4, ensure_ascii=False)

    resposta = {
        "message": "Doador criado com sucesso",  
    }
    return jsonify(resposta), 201

 

    with open('doadores.json', 'r') as f:
        doadores = json.load(f)
    
    doadores.append(dados)
    
    with open('doadores.json', 'w') as f:
        json.dump(doadores, f, indent=4)
    
    return jsonify(dados), 201

app.json.sort_keys = False
@app.route('/doadores', methods=['GET'])

@app.post('/estoque')
def cria_estoque():
    dados = request.get_json()

    if not dados.get('estoque'):
        return jsonify({"error": "O campo 'estoque' é obrigatório."}), 400
        

    with open ('estoque.json', 'r') as f:
        estoque = json.load(f)
    estoque.append(dados)

    with open ('estoque.json', 'w') as f:
        json.dump(estoque, f, indent=4, ensure_ascii=False)

    resposta = {
        "message": "Estoque criado com sucesso",  
    }
    return jsonify(resposta), 201

@app.post('/sangue')
def criar_sangue():
    dados = request.get_json()

    if not dados.get('sangue'):
        return jsonify({"error": "O campo 'sangue' é obrigatório."}), 400
        

    with open ('sangue.json', 'r') as f:
        sangue = json.load(f)
    sangue.append(dados)

    with open ('sangue.json', 'w') as f:
        json.dump(sangue, f, indent=4, ensure_ascii=False)

    resposta = {
        "message": "Sangue criado com sucesso",  
    }
    return jsonify(resposta), 201


def listar_doadores():
    
    with open('doadores.json', 'r') as f:
        dados = json.load(f)
    
    return jsonify(dados)
    
    
@app.route('/sangue', methods=['GET'])
def listar_sangue():
    
    with open('sangue.json', 'r') as f:
        sangue = json.load(f)
    
    return jsonify(sangue)
       
@app.route('/estoque', methods=['GET'])
def listar_estoque():

    with open('estoque.json', 'r') as f:
        estoque = json.load(f)
    
    return jsonify(estoque)





app.run()