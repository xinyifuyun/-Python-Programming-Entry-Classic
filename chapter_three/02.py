a = ("first", "second", "third")

print("The first element of the tuple is %s" % a[0])
print("The second element of the tuple is %s" % a[1])
print("The third element of the tuple is %s" % a[2])

print("%d" % len(a))
print(a[len(a) - 1])

b = (a, "b's second element")
print(b[1])
print(b[0][0])
print(b[0][2])
