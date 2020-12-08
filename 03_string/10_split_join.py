# to fill "-" in blank space for given string using  split and join method
def split_and_join(line):
        result= "-".join(line.split())
        return result

if __name__ == '__main__':
    line = input()
    print(split_and_join(line))