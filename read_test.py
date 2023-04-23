def read_keys():
    file = open("Keys.txt", mode='rb')
    fileContent = file.readlines()
    file.close()
    return fileContent
