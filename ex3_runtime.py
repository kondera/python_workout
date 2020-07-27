def run_timing():

    num_of_runs = 0
    total_time = 0

    while True:
        running_time = input("Enter 10 km run time: ")

        if not running_time:
            break

        try:
            total_time += float(running_time)
            num_of_runs += 1
        except ValueError:
            print("You passed wrong time")
            continue

    try:
        avg_time = total_time / num_of_runs
        print(f"Average of  {avg_time:.2f} over {num_of_runs} runs")
    except ZeroDivisionError:
        print("You didn't even run")


def float_slice(num: float, before: int, after: int) -> float:
    """Returns float consisting before integer digits and after
    decimal digits
    """
    integer_part = str(int(num // 1))
    decimal_part = str(num % 1)
    integer_part = integer_part[len(integer_part) - before :]
    decimal_part = decimal_part[: 2 + after]

    return float(integer_part) + float(decimal_part)


if __name__ == "__main__":
    run_timing()
    # print(float_slice(1234.5678, 2, 3))
