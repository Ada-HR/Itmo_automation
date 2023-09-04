a: int = 5
b: int = 'строка'
c: int = [1, 2]

def indent(s: str, width: int) -> str:
    return " " * (max(0, width - len(s))) + s


print(indent('123', 123))

def string_length(s: str = ' ') -> int:
    return len(s)
