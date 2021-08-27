# count char in string

def input_string():
    string = input("Enter something: ")
    return string

def count_char(string):
    count = 0
    for i in string:
        count += 1
    return count

string = input_string()
print(f"Length: {count_char(string)}")