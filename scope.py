x = 4
def foo():
    x = 5
    print(f"Outer: {x}")
    def inner():
        print(f"Inner: {x}")
    inner()

foo()
print(f"Global: {x}")