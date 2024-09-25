# file_handling_assignment.py
try:
    with open('my_file.txt', 'w') as file:
        file.write("Hello, this is line 1.\n")
        file.write("This is line 2 with a number: 42.\n")
        file.write("Line 3 is just a simple sentence.\n")
    print("File created and written successfully!")
except Exception as e:
    print(f"An error occurred during writing: {e}")
finally:
    print("Write operation completed.")


try:
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print("\nReading the file content:")
        print(content)
except FileNotFoundError:
    print("The file was not found.")
except Exception as e:
    print(f"An error occurred during reading: {e}")
finally:
    print("Read operation completed.")


try:
    with open('my_file.txt', 'a') as file:
        file.write("This is an appended line 4.\n")
        file.write("Appending line 5 with another number: 99.\n")
        file.write("Final appended line 6.\n")
    print("\nAdditional lines appended successfully!")
except Exception as e:
    print(f"An error occurred during appending: {e}")
finally:
    print("Append operation completed.")
