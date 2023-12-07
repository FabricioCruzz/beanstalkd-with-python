import json
import time
from pystalk import BeanstalkClient

HOST = "127.0.0.1"
PORT = 11300

# Instanciando o Beanstalkd na aplicação
client = BeanstalkClient(HOST, PORT)

id = 1
for i in range(1000):
    # Criando um objeto JSON
    message = {
    "id": id,
    "job_name":"Teste de Falhas",
    "course":"Sistemas de Informacao",
    "institution":"Univas"
    }
    
    with client.using("teste_falhas") as inserter:
        inserter.put_job(json.dumps(message))
    time.sleep(0.1)
    id += 1
    
client.close()
