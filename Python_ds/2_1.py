# 2 Data preparation
# 2_1 How to add an index field in python

list1 = ['apple', 'banana', 'orange', 'grape']
indexed_list = list(enumerate(list1))
for index, value in indexed_list:
    print(f'Index: {index}, Value: {value}')
