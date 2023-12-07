import time
from pystalk import BeanstalkClient

HOST = "127.0.0.1"
PORT = 11300

# Instanciando o Beanstalkd na app
client = BeanstalkClient(HOST, PORT)
client.watch("teste_carga")

for job in client.reserve_iter():
    # Processando trabalho da fila
    print(job.job_data)
    # Removendo o trabalho processado da fila
    client.delete_job(job.job_id)
    time.sleep(0.03)
client.close()
