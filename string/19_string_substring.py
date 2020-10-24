# to find the number of time a substring occurs in the given string

# Method 1
def count_substring(string, sub_string):
    count1 = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
                count1 += 1
    return count1

# Method 2

def match_substring(string, sub_string):
    match1 = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            match1 += 1
    return match1

if __name__ == '__main__':
    string = input("Enter a string: ").strip()
    sub_string = input("Enter a substring:").strip()
    print(count_substring(string, sub_string))
    print(match_substring(string, sub_string))
