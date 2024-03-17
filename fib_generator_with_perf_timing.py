from time import time


# Performance decorator
def performance(fn):
    def wrapper_fn(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"took {t2-t1}s")
        return result
    return wrapper_fn


# def fib_gen(up_to_nth_number):
#     prev_num = 0
#     curr_num = 0
#     for index in range(up_to_nth_number):
#         if index == 1:
#             prev_num = 1
#         next_num = prev_num + curr_num
#         prev_num = curr_num
#         curr_num = next_num
#         yield next_num


def fib_gen(up_to_nth_number):
    prev_num = 0
    curr_num = 1
    for index in range(up_to_nth_number):
        if index == 0:
            yield 0
        elif index == 1:
            yield 1
        else:
            next_num = prev_num + curr_num
            prev_num = curr_num
            curr_num = next_num
            yield next_num


def fib_gen2(up_to_nth_number):
    curr_num = 0
    next_num = 1
    for index in range(up_to_nth_number):
        yield curr_num
        old_curr_num = curr_num
        curr_num = next_num
        next_num = old_curr_num + next_num


def fib_row(up_to_nth_number):
    fib_row = []
    prev_num = 0
    curr_num = 1
    for index in range(up_to_nth_number):
        if index == 0:
            fib_row.append(0)
        elif index == 1:
            fib_row.append(1)
        else:
            next_num = prev_num + curr_num
            prev_num = curr_num
            curr_num = next_num
            fib_row.append(next_num)
    return fib_row


@performance
def print_gen_fib_numbers(up_to_nth_number):
    for number in fib_gen(up_to_nth_number):
        # print(number)
        continue


@performance
def print_gen_fib_numbers2(up_to_nth_number):
    for number in fib_gen2(up_to_nth_number):
        # print(number)
        continue


@performance
def print_fib_numbers(up_to_nth_number):
    for number in fib_row(up_to_nth_number):
        # print(number)
        continue


print_gen_fib_numbers(200000)
print_gen_fib_numbers2(200000)
print_fib_numbers(200000)
