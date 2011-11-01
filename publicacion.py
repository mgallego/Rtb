from usuario import Usuario
from time import time

class Publicacion:
    def __init__(self, client, post):
        self.post = post
        self.client = client

    def getPuntuacion(self):
        return 10

    def reblog(self):
        print "reblogueando: " + str(self.getAtributo("id"))
        print self.client.reblog_post("moisesgallego.tumblr.com", {"id":self.getAtributo("id"), "reblog_key":self.getAtributo("reblog_key")})

    def getAtributo(self, atributo):
        return self.post[atributo]

    def getUsuario(self):
        return Usuario(self.client.info(self.getAtributo("blog_name")+".tumblr.com"))

    def getAntiguedad(self):
        if int((int(time()) - self.getAtributo("timestamp")) /60) == 0:
            return 1
        return int((int(time()) - self.getAtributo("timestamp")) /60)

    
    def publicable(self):
        if self.getAtributo("note_count") / self.getAntiguedad() > 10:
            return True
