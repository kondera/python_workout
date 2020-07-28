def hex_output():
    hex_num = input("Enter a hex number to convert to decimal: ")
    dec_num = 0
    for p, d in enumerate(reversed(hex_num)):
        dec_num += int(d, 16) * (16 ** p)
    print(dec_num)


def triangle_name():
    name = input("Enter name: ")
    for i in range(1, len(name) + 1):
        print(name[:i])


if __name__ == "__main__":
    # hex_output()
    triangle_name()
