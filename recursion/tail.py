# Tail Recursion
# Recursive call happens after processing (last operation).

def tail_recursion(n):
    if n == 0:
        return
    print(n)
    tail_recursion(n - 1)