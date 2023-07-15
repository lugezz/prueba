# def topten():
#
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#
#
#
# values =  topten()
#
# print(values.__next__())
# print(values.__next__())

def basic_gen():
    yield 1
    yield 2
    yield 3
    yield 4


def topten():

    n = 1

    while n <= 10:
        sq = n * n
        yield sq
        n += 1


basic = basic_gen()

print(basic.__next__())
print(basic.__next__())
print(basic.__next__())
print(basic.__next__())
# print(basic.__next__())  Causes an error

values = topten()
print(type(values))

for i in values:
    print(i)
