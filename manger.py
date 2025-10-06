from contextlib import contextmanager




class Example():
    
    def __enter__(self):
        print("Enter")
        # self.file = ''''''


    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit")
        # self.close()

@contextmanager
def example2():
    print("Enter")
    try:
        yield
    finally:
        print("Exit")


if __name__ == "__main__":
    # with Example():

    #     # raise FileExistsError
    #     print("my actions")


    with example2():
        print("my actions")

