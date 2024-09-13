import random
# 2
# the orientation of the unique values in the set, in comparison to list\tuple, doesn't matter.
# it will print the values differently every time you run it
my_set = {'joseph', 'anna', 'baggie', 'joseph'}
print(my_set)
# therefore you can't call a value by its index

# 3
# the dict an the set both have unique keys, if you try adding the same key for a dict/
# or the same value for a set, it just 'run over' it
my_dict ={
    'apple': 1,
    'banana': 2,
    'banana': 3,
}
print(my_dict)

# 4
comp_set = {_ for _ in range(1, 101)}
print(comp_set)

# 5
my_list = [random.randint(100, 500) for i in range(50)]
print(my_list)
set_list = set(my_list)
print(f"there are {len(set_list)}/50 unique numbers in my_list")



