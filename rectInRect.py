import cv2
import numpy as np
# |----------------------------------------------------------------------------|
# check_box_in_box
# |----------------------------------------------------------------------------|
def check_box_in_box(boxList):
    '''
    
    '''
    img = np.zeros((1000,1000))

    
    finalBoxList = []
    insideBoxList = []
    nBox = len(boxList)
    for index1, box1 in enumerate(boxList):
        for index2, box2 in enumerate(boxList):
            if index1==index2:
                continue
#             # debug
#             print("box{} = {}".format(index1, box1))
#             print("box{} = {}".format(index2, box2))
#             # debug -ends
            x1,y1,xx1,yy1 = box1[0],box1[1],box1[0]+box1[2],box1[1]+box1[3]
            x2,y2,xx2,yy2 = box2[0],box2[1],box2[0]+box2[2],box2[1]+box2[3]
#             # debug
#             print(x1,y1,xx1,yy1)
#             print(x2,y2,xx2,yy2)
#             # debug -ends
            if box1 not in insideBoxList:
                if x1<x2 and y1<y2 and xx1>xx2 and yy1>yy2:
                    insideBoxList.append(box2)
    
#     # debug
#     print("insideBoxList = {}".format(insideBoxList))
#     # debug -ends
    for box in boxList:
        if box not in insideBoxList:
            finalBoxList.append(box)
            
#     # debug
#     print("finalBoxList = {}".format(finalBoxList))
#     # debug -ends

    
#     for (x,y,w,h) in finalBoxList:
#         cv2.rectangle(img, (x,y), (x+w,y+h), (255, 0, 0), 2)
#     for (x,y,w,h) in insideBoxList:
#         cv2.rectangle(img, (x,y), (x+w,y+h), (128,0, 0), 2)
#     
#     cv2.imshow("img",img)
#     cv2.waitKey(0)

    return finalBoxList
# |--------------------------------check_box_in_box---------------------------------|


if __name__ == '__main__':
    
    
    
    boxList = [[10,20,100,200], [300,300,100,100],[200,200,400,400],[250,250,20,20],[150,150,100,100], [30,40,50,50]]
    finalBoxList = check_box_in_box(boxList)