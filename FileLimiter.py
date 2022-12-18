# script to create a new file with less lines


active = True
while active:
    filename = input("what is the whole file name? ")
    try:
        with open(filename) as my_file:
            lines = my_file.readlines()
    except FileNotFoundError:
        print("No such file")
    else:
        active = False

filename2 = 'dataafterfiltering.csv'

lenghth = len(lines)

a=0
new_list = []
line1 = lines[0]
with open(filename2, 'w') as f:
    f.write(line1)

active = True
while active:
    sampling = input("Specify sampling in s ")
    try:
        b = int(sampling)
    except ValueError:
        print("This is not a number")
    else:
        active = False

for item in lines:
    a += 1
    if a == b:
        a = 0
        new_list.append(item)
        with open(filename2, 'a') as f:
            f.write(item)

print(len(new_list))
print(a)
