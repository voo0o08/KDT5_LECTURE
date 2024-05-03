def add(a, b): return a+b
def div(a, b): return a/b if b else None
print(__name__)

if __name__ == "__main__":
    print(f"funcs.py => __name__ : {__name__}")
    print(f"add(3, 4) {add(3, 4)}")
    print(f"div(3, 4) {div(3, 4)}")
