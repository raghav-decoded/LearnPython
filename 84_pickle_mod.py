'''
Pickling is the process of serializing an object.
Serializing means storing the object in the form of binary representation so it can be saved in our main memory. 

4Save objects
    extension = .pkl
    mode = binary
    dump(object,fileobject)
        put items into a file
    load(fileobject)
        load a pickle file of object type
    loads()
        s - str
        loads a string

'''
import pickle

# Pickling a python object
cars = ["Audi", "BMW", "Maruti Suzuki", "Harryti Tuzuki"]
file = "mycar.pkl"
fileobj = open(file, 'wb')
pickle.dump(cars, fileobj)
fileobj.close()

file = "mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))


# pickle.loads = ?




