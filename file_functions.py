import os

def writeInFile(line):
    current_path = os.getcwd()
    output_path = os.path.join(current_path, "./output")
    filename = os.path.join(output_path, "./output.txt")

    file1 = open(filename, "w")
    file1.writelines(str(line))
    file1.close()

def read_Image():
    current_path = os.getcwd()
    input_path = os.path.join(current_path, "./InputImages/")
    k = os.listdir(input_path)
    k.sort(reverse=True)
    print(k)

    filename = os.path.join(input_path, str(k[0]))

    return filename
