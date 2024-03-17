from collections.abc import Generator

def echo_round() -> Generator[int, float, str]:
    sent = 0
    while sent >= 0:
        sent = yield round(sent)
    return 'Done'

generator = echo_round()
next_value = next(generator)
next_value = generator.send(2.5)
print(next_value)
next_value = generator.send(3.5)
print(next_value)
try:
    next_value = generator.send(-1)
except StopIteration as s:
    print(s)
