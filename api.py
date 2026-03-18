from flask import Flask, json,request, jsonify

app = Flask(__name__)

app.json.sort_keys = False
@app.route('/doadores', methods=['GET'])

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