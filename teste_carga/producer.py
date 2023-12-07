import json
import time
from pystalk import BeanstalkClient

HOST = "127.0.0.1"
PORT = 11300

# Instanciando o Beanstalkd na app
client = BeanstalkClient(HOST, PORT)

id = 0
# Criando grande volume de mensagens
for i in range(5000):
    # Criando um objeto JSON
    message = {
        "id": id,
        "job_name":"Teste de Carga",
        "course":"Sistemas de Informacao",
        "institution":"Univas"
    }
    with client.using("teste_carga") as inserter:
        inserter.put_job(json.dumps(message))
    id += 1
    time.sleep(0.01)
    
client.close()
