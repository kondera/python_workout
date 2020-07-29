def strsort(word):
    return "".join(sorted(word))


def more_strsort(words):
    divided = words.split(" ")
    divided = sorted([strsort(word) for word in divided])
    print(f"Sorted: {*divided,} ")


if __name__ == "__main__":
    print(strsort("Python"))
    more_strsort("John Arbuckle and Garfield")
