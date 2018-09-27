def count_substring(string, sub_string):
    lenS = len(string)
    lenSS = len(sub_string)
    count=0
    for i in range(0, (lenS-lenSS)+1):
        print(i, i+lenSS)
        mySS = string[i:(i+lenSS)]
        print(mySS)
        if mySS==sub_string:
            count+=1
    return count


if __name__ == '__main__':
    string = "ABCDCDC"
    sub_string = "CDC"
    count = count_substring(string, sub_string)
    print(count)