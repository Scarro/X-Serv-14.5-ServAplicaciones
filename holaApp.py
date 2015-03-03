#!/usr/bin/python

import webapp

class holaApp(webapp.webApp):

    def process(self, parsedRequest):
        return("200 OK", "<html><body><h1>Hola mundo</h1></body></html>")

if __name__ == "__main__":
    testWeb = holaApp("localhost", 1234)

