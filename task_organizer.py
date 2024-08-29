import threading
import time
import random

def process_tasks(category, tasks):
    print(f"Processando tarefas da categoria: {category}.")
    for task in tasks:
        processing_time = random.uniform(0.5, 2)
        time.sleep(processing_time)
        print(f"Tarefa '{task}' da categoria '{category}' concluída em {processing_time:.2f} segundos.")

def main():
    tasks = {
        "Pessoal": ["Praticar Exercicios", "Ir ao supermercado", "Se Relacionar com Pessoas"],
        "Trabalho": ["Reunião com equipe", "Contatar Clientes", "Preparar relatório"],
        "Doméstico": ["Limpar a casa", "Dar comida ao pet", "Lavar roupa"]
    }
    
    threads = []
    for category, task_list in tasks.items():
        thread = threading.Thread(target=process_tasks, args=(category, task_list))
        threads.append(thread)
        thread.start()
  
    for thread in threads:
        thread.join()
    
    print("Todas as tarefas foram realizadas.")

if __name__ == "__main__":
    main()