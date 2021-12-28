def fun(task):
    print("the function is executing",task)

def doItMyWay(task):
    print('quickly performing',task)

def taskExecutor(mylist,callme):
    for x in mylist:
        print("Performing task setup and going to invoke")
        callme(x)
        print("performing the post activites and going to wrap the task")
        print('----------------------------------')

taskExecutor(['Building','Compiling','Packing','Deploying'],fun)
taskExecutor(['Building','Compiling','Packing','Deploying'],doItMyWay)
