print("hello")
my_var = 10
print(my_var)
my_name = "aviel"
print(my_name)
is_true = False
# my comment about this variable
my_list = ["aviel", "buskila", 31, True, my_name]
print(my_list[1])
my_dict = {"name": "aviel",
           "lname": "buskila",
           "age": 31,
            "is_married": True}
print(my_dict["name"])
print(my_dict.keys())
my_number = 5 * 2
my_other = 5 * "aviel"
print(my_other)

if my_number == 10:
    print("my_number")

fname = "aviel"
lname = "buskila"
print("hello " + fname + " " + lname)
print(f"hello {fname} {lname}")
print("hello %s %s" % (fname, lname))
