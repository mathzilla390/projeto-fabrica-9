
# 🛒 Lista de Compras API — organizando o supermercado (Flask)

Você foi contratado para criar uma **API de lista de compras** que ajude uma família (ou república de estudantes!) a **planejar, revisar e fechar** as compras do mês no supermercado.  
A ideia é prática e real: **cadastrar itens**, **listar**, **ajustar quantidade/categoria** e **remover** o que não será comprado — tudo por **HTTP** com respostas em **JSON**.

Este mini‑projeto usa **Flask** (Python) e foi pensado para estudantes do **ensino médio** que estão começando com **APIs REST**, **rotas**, **métodos HTTP** e **JSON** — com linguagem técnica, mas acessível. 🧑‍🍳🥦

---

## 🎬 Enunciado — A missão do dev
A turma está tendo dificuldades para organizar as compras: filmes na sexta, almoço de domingo, reposição do mês… sempre fica algo de fora.  
Seu trabalho é construir uma **API** que permita:

1. **Listar** todos os itens já cadastrados na lista de compras;  
2. **Adicionar** novos itens conforme forem lembrando;  
3. **Atualizar** informações (ex.: nome, quantidade, categoria, prioridade ou status de “comprado”);  
4. **Deletar** itens que não farão mais parte da compra.

Todas as respostas devem ser **JSON** bem formatado. O time vai usar **Insomnia/Postman/curl** para interagir.

> **Ideia de evolução**: futuramente a família quer **calcular o orçamento** da compra, **agrupar por corredor** (açougue, hortifruti, limpeza) e **marcar** itens como comprados no app.

---

## 🧠 Objeto de domínio: `Item`
Cada item da lista é um JSON no formato:

```json
{
  "id": 1,
  "nome": "Arroz 5kg",
  "quantidade": 2,
  "categoria": "Alimentos",
  "prioridade": "alta",
  "comprado": false
}
```
- `id` (int): gerado pela API  
- `nome` (str): **obrigatório**  
- `quantidade` (int ≥ 1): **obrigatório**  
- `categoria` (str): opcional (ex.: Alimentos, Higiene, Limpeza, Hortifruti…)  
- `prioridade` (str): opcional (`baixa` | `media` | `alta`)  
- `comprado` (bool): opcional, **padrão `false`**

---

## 🚦 Rotas (CRUD)
| Método | Rota           | Descrição                                         | Corpo (JSON)                                                                 | Códigos |
|------:|-----------------|---------------------------------------------------|------------------------------------------------------------------------------|--------:|
| GET   | `/items`        | Lista todos os itens                              | –                                                                            | 200     |
| GET   | `/items/<id>`   | Busca um item por `id`                            | –                                                                            | 200/404 |
| POST  | `/items`        | Adiciona novo item                                | `{ "nome", "quantidade", "categoria?", "prioridade?", "comprado?" }`         | 201/400 |
| PUT   | `/items/<id>`   | Atualiza **parcialmente** um item                 | Subconjunto de `{ "nome","quantidade","categoria","prioridade","comprado" }`| 200/400/404 |
| DELETE| `/items/<id>`   | Remove um item                                    | –                                                                            | 204/404 |
| GET   | `/health`       | Verifica se a API está ativa                      | –                                                                            | 200     |

> Observação: o `PUT` aceita **atualização parcial** (comportamento de `PATCH`) para facilitar a vida do iniciante.

---

## ✅ Critérios de aceitação (checklist)
- [ ] Rotas CRUD respondem com **JSON** e **status code** corretos  
- [ ] `POST` valida campos obrigatórios (`nome`, `quantidade >= 1`)  
- [ ] `id` é **gerado pela API** (o cliente não envia)  
- [ ] Erros claros: `400` (payload inválido) e `404` (não encontrado)  
- [ ] `DELETE` com **204 No Content** quando bem‑sucedido  
- [ ] Projeto roda com `python app.py` e tem `requirements.txt`

---

## 💻 Como rodar

**Pré‑requisito:** Python **3.10+**

```bash
# 1) (Opcional) Ambiente virtual
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 2) Instalar dependências
pip install -r requirements.txt

# 3) Iniciar a API
python app.py
# ou:
# flask --app app:app run --reload

# Teste rápido:
curl -s http://127.0.0.1:5000/health
```

---

## 🔎 Exemplos rápidos com `curl`

Listar itens:
```bash
curl -s http://127.0.0.1:5000/items | jq
```

Criar item:
```bash
curl -s -X POST http://127.0.0.1:5000/items   -H "Content-Type: application/json"   -d '{"nome":"Arroz 5kg","quantidade":2,"categoria":"Alimentos","prioridade":"alta"}' | jq
```

Buscar por id:
```bash
curl -s http://127.0.0.1:5000/items/1 | jq
```

Marcar como comprado (atualização parcial):
```bash
curl -s -X PUT http://127.0.0.1:5000/items/1   -H "Content-Type: application/json"   -d '{"comprado": true}' | jq
```

Deletar:
```bash
curl -i -X DELETE http://127.0.0.1:5000/items/1
```

---

## 🧠 Conceitos trabalhados
- HTTP e métodos **GET/POST/PUT/DELETE**  
- **JSON** como formato de troca de dados  
- Rotas e handlers com **Flask**  
- **Validação** básica e **códigos de status**  
- Modelagem simples de domínio (**Item**) e boas práticas de API

---

## 🚀 Próximos passos (para evoluir)
- Campos opcionais de **preço** e **loja**; cálculo de **orçamento total**  
- Filtros por **categoria** / **prioridade** / **comprado** em `/items`  
- **Paginação** para listas grandes  
- Persistência com **SQLite** (em vez de armazenar em memória)  
- **CORS** e um **frontend** simples que consome a API

---

## 📂 Estrutura sugerida
```
shopping-list-api/
├─ app.py
├─ requirements.txt
├─ README.md
├─ tests/
│  └─ test_app.py
├─ .gitignore
└─ LICENSE
```

---

## 📝 Licença
Projeto sob **MIT** — use, adapte e compartilhe. 🧺✨
