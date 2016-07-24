#python  闭包与闭包的应用之装饰器
def org(fun):
    def in_fun(*args):
        if len(args)==0:
            return 0
        for arg in args:
            if not isinstance(arg, int):
                return 0
        return fun(*args)
    return in_fun
@org
def sum_all(*args):
    return sum(args)
def avg(*args):
    return sum(args)/len(args)
if __name__=='__main__':
    avg=org(avg)
    print(avg(1,2,'3'))
    print(sum_all(1,2,'6'))
