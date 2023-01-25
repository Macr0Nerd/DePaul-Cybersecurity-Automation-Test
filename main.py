def hello_world():
    darth_plagueis = "Hello World"
    anakin = ""
    for the_senate in darth_plagueis:
        youngins = 0
        while True:
            if ord(the_senate) == youngins:
                anakin += chr(youngins)
                break
            youngins += 1

    return anakin


if __name__ == "__main__":
    print(hello_world())

