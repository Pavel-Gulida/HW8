
def add_one(some_list):
    some_list[-1] += 1
    for i in range(len(some_list)):
        if some_list[-1-i] < 10:
            return some_list
        some_list[-1-i] = 0
        if i == len(some_list) - 1:
            return [1] + some_list
        some_list[-2-i] = some_list[-2-i] + 1

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")