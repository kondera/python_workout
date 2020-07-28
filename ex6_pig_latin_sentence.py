from ex5_pig_latin import pig_latin


def pl_sentence(sentence):
    result = [pig_latin(word) for word in sentence.split()]
    return " ".join(result)


if __name__ == "__main__":
    print(pl_sentence("This is some random sentence."))
