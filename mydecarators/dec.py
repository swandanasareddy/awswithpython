def resourceHandler(fun):
    def logicController(*args,**kwargs):
        print('Checking the resource and its authenticity')
        print('Going to the actual function to run')
        fun(*args, **kwargs)
        print('Deallocating the memory allocated for the process')
        print('#####process terminated#####')
    return logicController