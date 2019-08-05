import os
from flask import render_template
import flask
import json
class Input():
    def __init__(self,length = None,oldWord = None,newWord = None,counter = None):
        self.length = length
        self.oldWord = oldWord
        self.newWord = newWord
        self.counter = counter
        

inputs = os.listdir("input")
outputs = os.listdir("output")

inputList = []
outputList = []


for i in range(0,len(inputs)):
    f = open("input\\"+inputs[i],"r")
    g = open("output\\"+outputs[i],"r")
    input = Input()
    input.length = f.readline()
    input.oldWord = f.readline()
    input.newWord = f.readline()
    input.counter = g.readline()
    inputList.append(input)





app = flask.Flask('my app')

if __name__ == "__main__":
    with app.app_context():
        rendered = render_template('raportTemplate.html', \
            title = "Raport", \
            inputList = inputList
            )
        print(rendered)
        
    

