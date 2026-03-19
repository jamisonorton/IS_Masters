# week 6
# Code along 3
while True:
    file_name = input("Enter a file name: ")
    try:
        fhandle = open(file_name, "r+")
        contents = fhandle.read()
        print(contents)

        while True:
            text = input("What do you want to write out? ")
            if text.lower() == "done":
                break

            fhandle.write(text + "\n")

    except Exception as ex:
        print(ex)

    else:
        break
