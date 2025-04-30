def main():
    with open("cooper.txt", "r") as f:
        contents = f.read()

    chapter1 = contents[1:500]
    with open("chapter1.txt", "w") as f:
        f.writelines(chapter1)

main()