class PyFun(object):
    def dict1(n):

        d = {}
        d["a"] = 1
        d["b"] = "c"

        for k in d.items():
            print(k)

    def nums():
        lst = []
        for x in range(9):  #0.... 8
            lst.append(x)

        print(lst)

    def itt(nums):
        for position, element in enumerate(nums):
            print(position, element)

PyFun.itt([4,3,23,2,3])