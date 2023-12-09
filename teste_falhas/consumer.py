import time
from pystalk import BeanstalkClient
from pystalk import BeanstalkError

class MyBeanstalkError(Exception):
    pass

HOST = "127.0.0.1"
PORT = 11300

client = BeanstalkClient(HOST, PORT)
client.watch("teste_falhas")

processed_count = 0

for job in client.reserve_iter():
    try:
        client.reserve_job(timeout=5)
        
        if job is None:
            print("No job received. Exiting...")
            break
        
        # Processando trabalho
        print(f"Processing job: {job.job_data}")
        
        time.sleep(0.2)
        
        # Excluindo trabalho da fila após processamento
        client.delete_job(job.job_id)
        
        # Simulando falha de conexão durante processamento das mensagens da fila
        if processed_count == 200:
            print("Simulating connection failure...")
            client.close()
            raise MyBeanstalkError("Connection failure!")
        
        processed_count += 1
    
    except MyBeanstalkError as ex:
        print(f"Error: {ex}")
        break
        
client.close()
