#!/usr/bin/python3
import add_0
a = 1
b = 2
print("<a {}> + <b {}> = ".format(a, b), end="")
result = add_0.add(a, b)
print("<add({}, {}) {}>".format(a, b, result))
