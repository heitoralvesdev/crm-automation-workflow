import requests

# Simulating sending a lead to a CRM via API
url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "name": "João Silva",
    "email": "joao@email.com",
    "status": "new_lead"
}

response = requests.post(url, json=data)

if response.status_code == 201:
    print("Lead enviado com sucesso!")
else:
    print("Erro ao enviar lead")
