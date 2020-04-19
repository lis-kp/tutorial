my_string1 = "book"

print(my_string1.upper())

my_string2 = "JAPAN"

print(my_string2.lower())

print("")

if my_string1.startswith("b"):
  print("my_string1 starts with \"b\"")
else:
  print("my_string1 does NOT starts with \"b\"")

if my_string2.endswith("S"):
  print("my_string2 ends with \"S\"")
else:
  print("my_string2 does NOT end with \"S\"")

print("")
mystring3 =  "  desk   "
print(mystring3.strip())