def simple_func1():
    pass

def simple_func2():
    return


def simple_func3():
    yield

gen_func = (i for i in range(100))


# print(type(simple_func1))
# print(type(simple_func1()))

# print(type(simple_func2))
# print(type(simple_func2()))

# print(type(simple_func3))
# print(type(simple_func3()))


# print(type(gen_func))


# def make_sum(val, m):
#     result = val
#     while True:
#         print(result)
#         result += m 


# make_sum(0, 1)


def make_sum(val, m):
    result = val
    while True:
        yield result
        result += m 


# print(make_sum(0, 1))

# for i in make_sum(0, 1):
#     print(i)


# gen = make_sum(0, 1)


# print(next(gen))

# print("какая-то логика")
# print(next(gen))

# print("какая-то логика")

# print(next(gen))

# print("какая-то логика")


task1 = make_sum(10, 1)
task2 = make_sum(100, 1)
task3 = make_sum(1000, 1)

iteration = 0
# while True:
#     print(next(task1))
#     print(next(task2))
#     print(next(task3))

#     if iteration == 10:
#         break

#     iteration += 1

from sys import getsizeof

# iter_obj = [ind for ind in range(1, 99999999999)]
gen_obj = (ind for ind in range(1, 99999999999))

# print(getsizeof(iter_obj))
print(getsizeof(gen_obj))


#  ----------------------------------------------
def read_file(file_name: str):
    with open(file_name) as f:
        return f.read().split("\n")
    

my_file = read_file("my.txt")

for row in my_file:
    ... 


def read_file(file_name: str):
    with open(file_name) as f:
        for row in f:
            yield row