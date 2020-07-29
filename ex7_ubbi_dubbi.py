def new_word(word, start):
    result = []
    for c in word[start:]:
        if c in "aeiou":
            result.append(f"ub{c}")
        else:
            result.append(c)

    return result


def ubbi_dubbi(word):
    result = []

    if word[0].isupper():
        result = [f"Ub{word[0].lower()}"] + new_word(word, 1)
    else:
        result = new_word(word, 0)

    return "".join(result)


if __name__ == "__main__":
    print(ubbi_dubbi("program"))
