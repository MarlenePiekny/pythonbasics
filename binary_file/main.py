
def create():
    open("zoo", "xb")


def write_into():

    data = [72, 69, 76, 76, 79, 33]
    bytes_array_data = bytearray(data)
    with open("zoo", "wb") as binary_file:
        binary_file.write(bytes_array_data)


def display():
    with open("zoo", "rb") as binary_file:
        byte = binary_file.read(1)
        while byte:
            print(byte)
            byte = binary_file.read(1)


def main():
    create()
    write_into()
    display()


if __name__ == '__main__':
    main()
    