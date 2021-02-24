'''Open a blank file in your text editor and write a few
lines summarizing what you’ve learned about Python so far. Start each line
with the phrase In Python you can.... Save the file as learning_python.txt in the
same directory as your exercises from this chapter. Write a program that reads
the file and prints what you wrote three times. Print the contents once by reading
in the entire file, once by looping over the file object, and once by storing
the lines in a list and then working with them outside the with block.'''


# Printing by reading in the entire file
with open('Chapter_10\learning_python.txt') as file_object:
    read_file = file_object.read()

    for i in range(1,4):
        print (read_file)

# Looping over the file Object
with open('Chapter_10\learning_python.txt') as file_object:
    read_file = file_object.readlines()

    for line in read_file:
        print (line.rstrip())

# Storing the lines in a list
with open('Chapter_10\learning_python.txt') as file_object:
    read_file= file_object.readlines()

for line in read_file:
    print(line.rstrip())