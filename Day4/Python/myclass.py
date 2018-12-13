#!/usr/bin/python

class Hello:
   
    def __init__(self):
       print ( 'Constructor' )
       self.x = 0
       self.y = 0

    def setValues(self, value1, value2):
        self.x = value1
        self.y = value2

    def printValues(self):
        print('Value of x is ' + str(self.x) )
        print('Value of y is ' + str(self.y) )


obj = Hello()
obj.setValues ( 10, 20 )
obj.printValues ( )
