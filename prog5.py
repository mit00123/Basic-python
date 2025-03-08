def myfunc():
    def message():
        return "how are you"
    return message
fun=myfunc()
print(fun())
