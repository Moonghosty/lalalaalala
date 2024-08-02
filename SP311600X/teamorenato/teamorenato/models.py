class Tarefa:
    def __init__(self,id,desc,concluido=False):
        self.id = id
        self.desc = desc
        self.concluido = concluido 

tarefas = []

t = Tarefa(1, "amar o renato")
tarefas.append(t)
t2 = Tarefa(2,"amar a andressa", True)
tarefas.append(t2)