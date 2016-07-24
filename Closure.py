#python  闭包
def sum_all(*args):
    return sum(args)
def avg(*args):
    return sum(args)/len(args)
def org(fun):
    def in_fun(*args):
        if len(args)==0:
            return 0
        for arg in args:
            if not isinstance(arg, int):
                return 0
        return fun(*args)
    return in_fun
if __name__=='__main__':
    sum_all=org(sum_all)
    print(sum_all(1,2,'6'))
