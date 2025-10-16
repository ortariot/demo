
# for ind in range(10):
#     print(ind)


class Range:

    def __init__(self, stop_value: int):
        self.stop_value = stop_value
        self.current = -1


    def __iter__(self):
        return self
    

    def __next__(self):
        if self.current < self.stop_value -1:
            self.current += 1
            return self.current
        raise StopIteration
    

# for ind in Range(10):
#     print(ind)



test_list = [1, 2, 3 , 4]

# index  = 0
# while True:
#     print(test_list[index])
#     index += 1


def my_for(cls, func):
    while True:
        try:
            value =cls.__next__()
            func(value)
        except StopIteration:
            break

my_for(Range(10), print)