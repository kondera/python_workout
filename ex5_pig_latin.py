def pig_latin(word):
    punctuations = "!;:,.?"
    punc = ""

    for i, c in enumerate(word):
        if c in punctuations:
            punc = c

    if word[0] in "aeiou":
        return f"{word.strip(punc)}way{punc}"
    else:
        return f"{word[1:].strip(punc)}{word[0]}ay{punc}"


if __name__ == "__main__":
    print(pig_latin("python"))
