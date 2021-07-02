def writeAline(filename, line):
    """
    This function write a string / line to a file
    :param filename, line :
    :return: None
    """
    with open(filename, mode='w') as myFile:
        myFile.write(line)