try:
    with open('sample/newfile.txt', 'a') as file:
        file.writelines(["\nThis is new file crested!2", "\nThis is another line to be added."])
except FileNotFoundError as e:
    print("ERROR", e)