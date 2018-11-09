from prompt_toolkit.keys import Key
class Sorting:

# |----------------------------------------------------------------------------|
# insertionSort
# |----------------------------------------------------------------------------|
    def insertionSort(self, arr):
        '''
        
        '''
        for j in range(1, len(arr)):
            key = arr[j]
            i=j-1
            while(i>=0 and arr[i]>key):
                arr[i+1]=arr[i]
                i=i-1
            #while -ends
            arr[i+1]=key
        #for -ends
        return arr
                
        
# |--------------------------------insertionSort---------------------------------|
    
















if __name__ == '__main__':
    arr = [6,3,1,2,4,1]
    sorting = Sorting()
    sortedArr = sorting.insertionSort(arr)
    print(sortedArr)