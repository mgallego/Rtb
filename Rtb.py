#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pyblr
import conector
from publicacion import Publicacion 
from usuario import Usuario
import time

client = pyblr.Pyblr(conector.Conector().getConexion())

posts =  client.dashboard({"limit":50, "type":"photo", "notes_info":"false"})

while True:

    for post in posts["posts"]:
        publicacion = Publicacion(client, post)
        print "RATIO: " + str(publicacion.getAtributo("note_count") / publicacion.getAntiguedad())
        print publicacion.getAtributo("post_url")
        
        if publicacion.publicable() :
            publicacion.reblog()
            
    time.sleep(1800)
