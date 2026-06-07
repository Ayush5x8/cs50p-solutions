def main():
    name = input("what is your name? ")
    print(greet(name))

def greet(to):
    return "hello, " + to

main()