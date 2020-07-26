def mysum(*nums):
    result = 0
    for num in nums:
        result += num
    return result


def mysum_with_list(lst, num=0):
    result = num
    for num in lst:
        result += num
    return result


def average_of_lst(lst):
    return mysum_with_list(lst) / len(lst)


def length_of_words(lst):
    shortest, longest, mean = len(lst[0]), len(lst[0]), len(lst[0])
    for word in lst[1:]:
        if len(word) < shortest:
            shortest = len(word)
        elif len(word) > longest:
            longest = len(word)
        mean += len(word)

    mean /= len(lst)

    return shortest, longest, mean


def sum_with_objects(*args):
    result = 0
    for obj in args:
        try:
            result += obj
        except TypeError:
            continue

    return result


if __name__ == "__main__":
    print(mysum(10, 20, 30, 40))
    print(mysum_with_list([10, 20, 30], 40))
    print(average_of_lst([10, 20, 30, 40]))
    print(length_of_words(["abc", "word", "longest", "test"]))
    print(sum_with_objects("abc", 4, 3.5, [4, "a"], (1, 2)))
