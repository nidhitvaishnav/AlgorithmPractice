def findMaxLog(domain, logs):
    myDict = {}
    for myStr in logs:
        myLen=len(myStr)
        if myLen>0 and domain in myStr:
            date = myStr.split(domain)[1]
            date=date[:8]
            if (date.isdigit() and len(date)==8):
                if date in myDict:
                    myDict[date]+=1
                else:
                    myDict[date]=1
    if len(myDict)==0:
        return None
    ans =  max(myDict.keys(), key=(lambda k: myDict[k]))
    print(myDict)
    return ans
    
if __name__ == '__main__':
    domain = "@solution1.com"
    logs = ["abc@solution1.com21201212", "sfsdsdfd@solution1.com20101010dgiu","ae@solution1.com20101010dgiu"]
#     logs = ["abc@solution1.com20193242", "df@solution1.com20181212","df@solution1.com20181212"]
    ans = findMaxLog(domain, logs)
    print(ans)
