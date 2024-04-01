def create_file():
    try:
      
        with open("my_file.txt", "w") as file:
            # Write at least three lines of text to the file
            file.write("Line 1: This is a sample line.\n")
            file.write("Line 2: 12345\n")
            file.write("Line 3: Python is awesome!\n")
        print("File 'my_file.txt' created successfully.")
    except PermissionError:
        print("Permission denied. Unable to create file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File creation process completed.\n")


def read_file():
    try:

        with open("my_file.txt", "r") as file:
            print("Contents of 'my_file.txt':")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found. Unable to read.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File reading process completed.\n")


def append_to_file():
    try:

        with open("my_file.txt", "a") as file:

            file.write("Line 4: Appended line 1\n")
            file.write("Line 5: 67890\n")
            file.write("Line 6: Python is versatile!\n")
        print("Content appended to 'my_file.txt' successfully.")
    except PermissionError:
        print("Permission denied. Unable to append to file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File appending process completed.\n")



def main():
    create_file()
    read_file()
    append_to_file()


if __name__ == "__main__":
    main()
