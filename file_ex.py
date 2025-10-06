big_file = open(file="hello_world_some_times.txt", mode="r")
# print(big_file.readlines())
for line in big_file.readlines():
    print(line)

print(type(big_file))
