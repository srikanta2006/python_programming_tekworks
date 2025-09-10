def count_words(line):
    words = line.split()
    print("Number of words:", len(words))

line = input("Enter the line: ")
count_words(line)
