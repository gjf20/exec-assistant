def greeting():
    return("hello world")


class HelloWorld:
    def greeting(self):
        print(self)
        return "hello world"


if __name__ == '__main__':
    my_world = HelloWorld()
    print(my_world.greeting())
    print(greeting())
