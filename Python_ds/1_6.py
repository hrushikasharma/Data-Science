# 1_6 Accessing variables and records in python
a = "Apples"
b = 5
my_list = [1, 2, 3, 5]
my_tuple = (2, 3, 4)
print(a)
print(b)
print(my_list[0])
# accessing record in a list
records = [
    {'id': 1, 'name': 'Hrushika', 'age': 25},
    {'id': 2, 'name': 'Hitanshi', 'age': 30},
    {'id': 3, 'name': 'Pranshu', 'age': 22}
]

first_record = records[0]
print("First Record:", first_record)
hrushika_age = records[0]['age']
print("hrushika's Age:", hrushika_age)

