def greet():
    print("hello world")


class HelloWorld:
    def greet(self):
        print("hello world")
        print(self)


if __name__ == '__main__':
    my_world = HelloWorld()
    my_world.greet()
    greet()
