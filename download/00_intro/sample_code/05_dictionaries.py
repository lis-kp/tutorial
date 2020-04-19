my_dict = {"olivia": 22, "maria": 30, "sophia": 18, "emily": 45}

my_dict["rachel"] = 15

print(len(my_dict))
print(my_dict["emily"])
print("")

if "elizabeth" in my_dict:
  print("elizabeth exists in my_dict")

print("my_dict sorted by key")
for key, value in sorted(my_dict.items()):
  print('{:s} --> {:d}'.format(key, value))

print("")
print("my_dict sorted by value")
for key, value in sorted(my_dict.items(), key=lambda x:x[1]):
  print('{:s} --> {:d}'.format(key, value))