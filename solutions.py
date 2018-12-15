### Problem 3
def get_min_missing_val(arr):
    val=1
    while val in arr:
        val+=1
    return val
    
print(get_min_missing_val([1,1,1,1]))

### Problem 4
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(f):
    def car_helper(a,b):
        return a
    return f(car_helper)

def cdr(f):
    def cdr_helper(a,b):
        return b
    return f(cdr_helper)

print(car(cons(3,4)))
print(cdr(cons(3,4)))