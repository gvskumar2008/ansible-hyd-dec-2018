#!/usr/bin/python

def sayHello(msg):
  print ( 'Hello ' + str(msg) )

def add ( value1, value2 ):
   return value1 + value2

sayHello( 'Python!' )
sayHello( 10 )
sayHello ( 1.434 )

print ( add ( 'Hello', 'Python' ) )
print( add ( 10, 20 ) )
print ( add ( 100.5, 200.5 ) )
