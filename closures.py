
a=888
def outer(param):
    print(param)
    a=230
    print(a)
    def inner(inside):
        a=350
        print("Processing inner and outer together {} {} {}".format(param,inside,a))
    print('outer',a)
    return inner

outer("India")("Asia")

store=outer("China")

store("Asia")
store("Big Country")
store("Near to India")