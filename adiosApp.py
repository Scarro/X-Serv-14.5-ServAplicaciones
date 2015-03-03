#!/usr/bin/python

import webapp

class adiosApp(webapp.webApp):

    def process(self,parsedRequest):
        return("200 OK", "<html><body><h1>Adios mundo</h1></body></html>")
    
if __name__ == "__main__":
    testWeb = adiosApp("localhost",1234)


