import os

ab = os.get_terminal_size().columns
read_data = input("enter you string")
print(read_data)
print(read_data.center(ab).title())
print(read_data.rjust(ab))
print(read_data.ljust(ab))