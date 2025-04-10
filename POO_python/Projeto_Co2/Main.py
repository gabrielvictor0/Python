from flask import Flask, jsonify, make_response, request
from Db import Ambiente

app = Flask("ambientes")

@app.route("/ambientes", methods=['GET'])
def get_ambientes():
    return Ambiente

@app.route("/ambientes/<int:id>", methods=['GET'])
def get_ambientes_id(id):
    for ambiente in Ambiente:
        if ambiente.get("id") == id:
            return jsonify(ambiente)

@app.route('/ambientes', methods=['POST'])
def post_ambiente():
    ambiente = request.json
    Ambiente.append(ambiente)
    return make_response(
        jsonify(mensagem='Ambiente cadastrado com sucesso', ambiente= ambiente)
    )

@app.route('/ambientes/<int:id>', methods=['PUT'])
def put_ambiente(id):
    ambiente_atualizado = request.get_json()
    for indice, ambiente in enumerate(Ambiente):
        if ambiente.get('id') == id:
            Ambiente[indice].update(ambiente_atualizado)
            return jsonify(Ambiente[indice])
        
@app.route('/ambientes/<int:id>', methods=['DELETE'])
def delete_ambiente(id):
    for indice, ambiente in enumerate(Ambiente):
        if ambiente.get('id') == id:
            del Ambiente[indice]
            return jsonify({"mensagem:" : "EXCLUIDO"})

app.run(port=5000, host='localhost')
