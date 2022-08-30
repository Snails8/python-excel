
class MyClass():
    def __init__(self, message) :
        self.value = message + ':init'


instance = MyClass("Hello")
print(instance.value)