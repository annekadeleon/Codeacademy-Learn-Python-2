garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

#takes string garbled and removes "X"s
message = filter(lambda x: x != "X", garbled)

#prints I am another secret message!
print message
