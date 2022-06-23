def thing1(name):
    print("Welcome to thing 1", name)

    def thing2():
        print("welcome to thing 2", name)
    thing2()


thing1("Jacob")