
import unittest
from app import app, ITEMS, PRIORIDADES

class ShoppingListApiTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        # Reset do seed para previsibilidade
        ITEMS.clear()
        ITEMS.extend([
            {"id": 1, "nome": "Arroz 5kg", "quantidade": 2, "categoria": "Alimentos", "prioridade": "alta", "comprado": False},
            {"id": 2, "nome": "Detergente", "quantidade": 3, "categoria": "Limpeza", "prioridade": "media", "comprado": False},
            {"id": 3, "nome": "Banana prata", "quantidade": 12, "categoria": "Hortifruti", "prioridade": "baixa", "comprado": False},
        ])

    def test_health(self):
        r = self.client.get('/health')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.get_json()["status"], "ok")

    def test_list_items(self):
        r = self.client.get('/items')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.get_json()), 3)

    def test_get_item_ok(self):
        r = self.client.get('/items/1')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.get_json()["id"], 1)

    def test_get_item_404(self):
        r = self.client.get('/items/999')
        self.assertEqual(r.status_code, 404)

    def test_create_item_ok(self):
        payload = {"nome": "Feijão 1kg", "quantidade": 1, "categoria": "Alimentos", "prioridade": "media"}
        r = self.client.post('/items', json=payload)
        self.assertEqual(r.status_code, 201)
        self.assertEqual(r.get_json()["nome"], "Feijão 1kg")
        self.assertIn("id", r.get_json())

    def test_create_item_400(self):
        r = self.client.post('/items', json={"nome": "Sem Quantidade"})
        self.assertEqual(r.status_code, 400)

    def test_update_item_ok(self):
        r = self.client.put('/items/1', json={"comprado": True})
        self.assertEqual(r.status_code, 200)
        self.assertTrue(r.get_json()["comprado"])

    def test_update_item_400(self):
        r = self.client.put('/items/1', json={"quantidade": 0})
        self.assertEqual(r.status_code, 400)

    def test_delete_item_ok(self):
        r = self.client.delete('/items/2')
        self.assertEqual(r.status_code, 204)

    def test_delete_item_404(self):
        r = self.client.delete('/items/999')
        self.assertEqual(r.status_code, 404)

if __name__ == '__main__':
    unittest.main()
