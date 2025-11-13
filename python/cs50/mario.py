for _ in range(3):
    print("#")

def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")


main()


def main():
    print_row(4)

def print_row(width):
    print("?" * width)


main()


def main():
    print_square(3)

def print_square(size):

    # for each row in square
    for i in range(size):
        # for each brick in row
        for j in range(size):
            # Print brick
            print("#", end="")
        print()


main()