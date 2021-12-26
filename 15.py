what_to_print = "hello world!"
list_of_names = ["Michael", "Noam", "Lior", "Amichai"]
amount_of_prints = 4
for i in range(1, amount_of_prints):
    print(str(i + 1) + ") " + what_to_print)

for i in range(len(list_of_names)):
    print(list_of_names[i])

for name in list_of_names:
    if name == "Hen":
        break

for name in list_of_names:
    if name == "Hen":
        break

for name in list_of_names:
    if name == "Hen":
        continue
    print(name)

a = 0
while a < 10:
    print(a)
    a = a + 1


for i in range (1,101):
    if i % 7 == 0 or "7" in str(i):
        continue
    print(i)

for i in range (1,101):
    if i % 7 != 0 and not "7" in str(i):
        pass
    else:
        print("hey")
    print(i)

a = "a"
while a != "q":
    a = input("enter q or not: ")

else:
    print("finished succesfully")

if i in range(5):
    print(i)
else:
    print("finished successfully")