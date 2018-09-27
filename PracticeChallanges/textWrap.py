def wrap(string, max_width):
    length = len(string)
    outStr = ""
    for i in range(0,length,max_width):
        myStr = string[i:i+max_width]
        outStr+=myStr+"\n"
    return outStr

if __name__ == '__main__':
    string = input()
    max_width = int(input())
    result = wrap(string, max_width)
    print(result)