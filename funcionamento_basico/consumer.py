import time
from pystalk import BeanstalkClient

HOST = "127.0.0.1"
PORT = 11300

client = BeanstalkClient(HOST, PORT)
client.watch("funcionamento_basico")

for job in client.reserve_iter():
    # Reservando um trabalho antes de colocá-lo como READY
    # Após um tempo o trabalho passa de RESERVED para READY
    client.reserve_job(timeout=5)
    
    # Colocando um trabalho em estado de BURIED
    client.bury_job(job.job_id)
    time.sleep(0.5)
    
    # Trabalho sendo colocado de volta na fila
    client.kick_job(job.job_id)
    time.sleep(0.2)
    
    # Processando trabalho
    print(f"Processing job: {job.job_data}")
        
    time.sleep(0.3)
        
    # Excluindo trabalho da fila após processamento
    client.delete_job(job.job_id)
client.close()
