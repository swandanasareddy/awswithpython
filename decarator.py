from mydecarators import resourceHandler

@resourceHandler
def process(file):
    print('Playing with resources here that is', file)
    print('manipulating and writing the resources')

@resourceHandler
def dbactivity(db):
    print('Working with db resources')
    print('Playing with db data')

process('file name e.txt')
dbactivity('db')

