class Usuario:
    def __init__(self, usuario):
        self.usuario = usuario

    def getAtributo(self, atributo):
        return self.usuario["blog"][atributo]
