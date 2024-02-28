tuple1 = ("Orange", (10, 20, 30), (5, 15, 25))
value_20 = tuple1[1][1]
print(value_20)

tuple2 = (10, 20, 30, 40)
a = tuple2[0]
b = tuple2[1]
c = tuple2[2]
d = tuple2[3]

print(a)
print(b)
print(c)
print(d)

tuple1 = (11, 22)
tuple2 = (99, 88)

tuple1, tuple2 = tuple2, tuple1

print("tuple 1:", tuple1)
print("tuple 2:", tuple2)