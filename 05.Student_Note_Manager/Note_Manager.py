print("======STUDENTS NOTES MANAGER======")


menu = (
    "1. Write new notes\n2.Add more notes\n3.Read all notes.\n4.Delete content\n5.Exit"
)

while True:
    print(menu)

    choice = int(input("Select your choice: "))

    filename = input("Enter Filename: ")
    match choice:
        case 1:
            with open(filename, "w") as file:
                note = input("Enter your notes ")
                file.write(note)
                print("note saved sucessfully!!")
        case 2:
            with open(filename, "a") as file:
                add = input("Enter your additional notes: ")
                file.write("\n" + add)
                print("Additional notes saved !!")
        case 3:
            try:
                with open(filename, "r") as file:
                    print(file.read())
            except FileNotFoundError:
                print("file doesn,t exists make file or write notes first")
        case 4:
            with open(filename, "w") as file:
                pass
                print("all content from file is deleted !!")
        case 5:
            print("thank you")
            break

        case _:
            print("Invalid choice")
