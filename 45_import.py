'''
import sys
print( sys.path)
'''
from sklearn.ensemble import RandomForestClassifier
print(RandomForestClassifier())

'''
from file2 import a
print(a)
'''
import file2
print(file2.a)

file2.printjoke("This is me")
  
