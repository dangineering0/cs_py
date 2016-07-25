# @return free times
def merge(nums):
    free = []
    lst = []
    for l in nums:
        lst.extend(l)


    sorted(lst, key=lambda x: x[0])

    print list(lst)

    reduced = red(lst)

    print reduced
    #return find_free(reduced)

def f(x,y):
    if x[0]==y[0]:
        return (x[0], max(x[1], y[1]))
    if x[1] > y[0]:
        return (x[0], max(x[1], y[1]))
    elif x[1] == y[0]:
        return (x[0], y[1])
    else:
        return [(x,y), (x,y)]


# @param sorted list of times
# @return list of combined intervals
def red(lst):
    return reduce(f, lst)


def find_free(lst):
    return lst

print(merge(
    [[(1,2),(3,4)],[(4,10), (20,30)]]))
