from flask import Flask, jsonify,request
app = Flask(__name__)

itens = [{"id": 1, "nome": "Arroz 5kg", "quantidade": 2, "categoria": "Alimentos", "prioridade": "alta", "comprado": False},
    {"id": 2, "nome": "Feijão 1kg", "quantidade": 10, "categoria": "Alimentos", "prioridade": "alta", "comprado": False}]

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify({"itens": itens, "total": len(itens)}), 200

@app.route("/items/<int:id>", methods=["PUT"])
def update_item(id):
    dados = request.get_json()
    for item in itens:
        if item["id"] == id:
            item.update(dados)
            return jsonify({"mensagem": "Item atualizado com sucesso!", "item": item}), 200

    return jsonify({"erro": "Item não encontrado!"}), 404

@app.route("/items/<int:id>", methods=["DELETE"])
def delete_item(id):
    if item['id'] == id:
        return jsonfy({'mensage': 'item deletado'})
    return jsofy({'erro':'item não encontrado'}),404
