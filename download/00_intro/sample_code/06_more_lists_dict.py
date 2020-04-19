my_list = [1,2,"3","four", "four"]
my_set = set(my_list)
my_dict = {"olivia": 22, "maria": 30, "sophia": 18, "emily": 45}

print(my_list)
print(my_set)

print("")

for key, value in sorted(my_dict.items()):
  print('{:s} --> {:d}'.format(key, value))