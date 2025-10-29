from flask import Flask, jsonify

app = Flask(__name__)

itens = [
    {"id": 1, "nome": "Arroz 5kg", "quantidade": 2, "categoria": "Alimentos", "prioridade": "alta", "comprado": False},
    {"id": 2, "nome": "Feijão 1kg", "quantidade": 10, "categoria": "Alimentos", "prioridade": "alta", "comprado": False}
]

@app.route("/items", methods=["GET"])
def get_items():
    """Retorna todos os itens da lista."""
    return jsonify({"itens": itens, "total": len(itens)}), 200


@app.route("/items/<int:id>", methods=["GET"])
def get_item_by_id(id):
    """Retorna um item específico pelo ID."""
    for item in itens:
        if item["id"] == id:
            return jsonify({"mensagem": "Item encontrado!", "item": item}), 200
    return jsonify({"erro": "Item não encontrado!"}), 404

if __name__ == "__main__":
    app.run(debug=True)
