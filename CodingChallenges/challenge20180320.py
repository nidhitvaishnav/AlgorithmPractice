'''
#####Intuit#####

Introduction
SUppose you are creating an internal networking site for your company. You have two data sets to work with. The first data set is the employees at your company, and the second is all the pairs of employees who are virtually friends so far. It does not matter which employee's ID is in which column; the friendships are bidirectional.

The problem
You're curious how employees are using your site. Specifically, you want to know how people between different departments are interacting.

Write a function that returns a data structure that tracks, for each department: how many employees are in that department, and how many of those employees have friends in other departments.

Note for example that Carla (ID: 6) is only friends with fellow Engineering employees. So while she DOES count towards the total number of employees in Engineering, she DOES NOT count towards the number of employees with friends outside the department.
'''



def get_employee_stats(employees, friendships):
    # IMPLEMENTATION GOES HERE
    #initializing dict and list
    networkDict={}
    employeesList = []
    empID=[]
    #reading employees data and storing them in networkDict
    for emp in employees:
        empDetail = emp.split(",")
        employeesList.append(empDetail)
        empID.append(empDetail[0])
        
        if empDetail[2] not in networkDict.keys():
            networkDict[empDetail[2]]={"employees":1, "employees_with_outside_friends":0}
        else:
            networkDict[empDetail[2]]["employees"]+=1
        #if empDetail -ends
    #for emp -ends
    
    #processing friendships data
    empFriendList = []
    for data in friendships:
        friend1, friend2 =data.split(",")
        
        emp1 = empID.index(friend1)
        emp2 = empID.index(friend2)
        

        if (employeesList[emp1][2]!=employeesList[emp2][2]):
            if (employeesList[emp1][0] not in empFriendList):
                networkDict[employeesList[emp1][2]]['employees_with_outside_friends']+=1
                empFriendList.append(friend1)
            #if -ends
            if (employeesList[emp2][0] not in empFriendList):
                networkDict[employeesList[emp2][2]]['employees_with_outside_friends']+=1
                empFriendList.append(friend2)
            #if -ends
        #if -ends
    #for data -ends

    return networkDict

    
    



if __name__ == '__main__':
    employees = [
            "1,Richard,Engineering",
            "2,Erlich,HR",
            "3,Monica,Business",
            "4,Dinesh,Engineering",
            "6,Carla,Engineering",
            "9,Laurie,Directors"
        ]
    friendships = [
            "1,2",
            "1,3",
            "1,6",
            "2,4"
        ]
    # debug
    print("employees = {}".format(employees[0]))
    # debug -ends
    
    # debug
    print("friendships = {}".format(friendships))
    # debug -ends

 
    network_dict = get_employee_stats(employees, friendships)
    # debug
    print("network_dict = \n{}".format(network_dict))
    # debug -ends
