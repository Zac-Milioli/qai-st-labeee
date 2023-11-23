
class PeR:
    def __init__(self):
        self.id_pergunta: list = None
        self.pergunta: list = None
        self.resposta: list = None
        self.json_to_send: dict = None
    
    def save_PeR(self):
        dataframeable = {'ID': self.id_pergunta, 'Perguntas': self.pergunta, 'Respostas': self.resposta}
        self.json_to_send = dataframeable

    def mail_to_luiza(self):
        pass

class Person:
    def __init__(self):
        self.email: str = 'No email'
        self.name: str = 'No name'
