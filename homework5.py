immutable_va = 1, 2,  "World"
print(immutable_va)

#stempl= "Factori" , 56
# print(immutable_va+stempl)
# "изменить кортеж не получится для более недёжной защиты элиментов данных-баз, особенность кортежа- занамает меньше места "

mutable_list = (100, [99, 88], "Stop") + (101, 102)
print(mutable_list)
mutable_list [1][1]= 99
print(mutable_list)
