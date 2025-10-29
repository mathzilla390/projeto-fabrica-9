from flask import Flask, jsonify, request, Response

app = Flask(__name__)

# --- Base de Dados (Lista de Compras em Memória) ---
lista_compras = [
    {
        "id": 1, 
        "nome": "Pão de Forma", 
        "quantidade": 1, 
        "categoria": "Alimentos", 
        "prioridade": "media", 
        "comprado": False
    }
]
proximo_id = 2 
@app.route("/health", methods=["GET"])
def health_check():
    """Verifica se a API está ativa."""
    return jsonify({"status": "API de Lista de Compras Online!"}), 200
@app.route("/items", methods=["GET", "POST"])
def items_collection():
    global proximo_id
    if request.method == "GET":
        return jsonify(lista_compras), 200
    elif request.method == "POST":
        dados = request.get_json()
        if not dados or "nome" not in dados or "quantidade" not in dados:
            return jsonify({"erro": "Campos 'nome' e 'quantidade' são obrigatórios."}), 400
        try:
            quantidade = int(dados["quantidade"])
            if quantidade < 1:
                return jsonify({"erro": "A 'quantidade' deve ser um número inteiro maior ou igual a 1."}), 400
        except ValueError:
             return jsonify({"erro": "O campo 'quantidade' deve ser um número inteiro."}), 400

        novo_item = {
            "id": proximo_id,
            "nome": dados["nome"],
            "quantidade": quantidade,
            "categoria": dados.get("categoria", "Outros"), 
            "prioridade": dados.get("prioridade", "baixa"), 
            "comprado": dados.get("comprado", False)     
        } 
        lista_compras.append(novo_item)
        proximo_id += 1 
        return jsonify(novo_item), 201
@app.route("/items/<int:item_id>", methods=["GET", "PUT", "DELETE"])
def item_resource(item_id):  
    item = next((i for i in lista_compras if i["id"] == item_id), None)

    if item is None:
        return jsonify({"erro": f"Item com ID {item_id} não encontrado na lista."}), 404

    if request.method == "GET":
        return jsonify(item), 200
    elif request.method == "PUT":
        dados_atualizados = request.get_json()
        if not dados_atualizados:
             return jsonify({"erro": "Nenhum dado fornecido para atualização."}), 400
        if 'nome' in dados_atualizados:
            item['nome'] = dados_atualizados['nome']
        
        if 'quantidade' in dados_atualizados:
             try:
                nova_qtd = int(dados_atualizados['quantidade'])
                if nova_qtd < 1:
                     return jsonify({"erro": "A 'quantidade' deve ser >= 1."}), 400
                item['quantidade'] = nova_qtd
             except ValueError:
                 return jsonify({"erro": "O campo 'quantidade' deve ser um número inteiro."}), 400
        if 'categoria' in dados_atualizados:
            item['categoria'] = dados_atualizados['categoria']
        
        if 'prioridade' in dados_atualizados:
            item['prioridade'] = dados_atualizados['prioridade']  
        if 'comprado' in dados_atualizados and isinstance(dados_atualizados['comprado'], bool):
            item['comprado'] = dados_atualizados['comprado']
        return jsonify(item), 200
    elif request.method == "DELETE":
        global lista_compras
        lista_compras = [i for i in lista_compras if i["id"] != item_id]
        return Response(status=204)
if __name__ == '__main__':
    app.run(debug=True)