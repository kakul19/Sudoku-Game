#Function to load sudoku from the file
def load_sudoku(level):
    count=0
    
    #Selecting file to read for each level
    if(level==1):
        f = open("level1.txt", "r")
    else:
        f = open("level2.txt", "r")
        
    #Initializing array to store sudoku 
    arr=[]
    
    #Reading one by one entry from the file and appending in the array
    for i in range(9):
        row=[]
        for j in range (9):
            x=f.read(1)
            
            #If new line is read, read the next character
            if(x=='\n'):
                x=f.read(1)
                
            #Store the number of missing values
            if(x=='0'):
                count=count+1
                
            row.append(int(x))
            
        arr.append(row)
    return [arr,count]

#Function to print sudoku
def print_sudoku(arr):
    
    #Traverse all the rows and columns and print each element of array
    for i in range(9):
        for j in range(9):
            if(arr[i][j]==0):
                print(" "),
            else:
                print(arr[i][j]),
        print("\n"),

#Function to check if the entered number is correct or not
def check_input(arr,num,r,c):
    r=r-1
    c=c-1
    
    #If entered number matches to any number in the same row return False
    for x in range(9):
        if(x!=c):
            if(arr[r][x]==num):
                return False

    #If entered number matches to any number in the same column return False
    for x in range(9):
        if(x!=r):
            if(arr[x][c]==num):
                return False
            
    #Compute the 3x3 block it belongs to
    row=r/3
    col=c/3
    
    #If entered number matches to any number in the same blcck return False
    for x in [3*row,(3*row)+1,(3*row)+2]:
        for y in [3*col,(3*col)+1,(3*col)+2]:
            if(x!=r and y!=c):
                if(arr[x][y]==num):
                    return False
     
    #If entered number is incorrect, store it in array   
    arr[r][c]=num        
    return True
    
print("Let's Play Sudoku ! \n")

while True:
    
    #Take valid input for Level number
    level=" "
    
    #Continue until valid input is entered
    while(level!='1' and level!='2'):
        level = raw_input("\nChoose the level you want to play\n1) Level 1\n2) Level 2\n\n")
        if(level!='1' and level!='2'):
            print("\nInvalid Input")
    level=int(level)
    [arr,count]=load_sudoku(level)
    print("\n")
    print_sudoku(arr)

    for i in range(count):
            
        valid_entry=0
        
        while (valid_entry==0):
            
            #Take valid input for row and column number of the entry to be filled
            print("\nEnter the row and column number of entry you want to fill")
            valid=0
            
            #Continue until valid row input is entered
            while(valid==0):
                r=raw_input("\nEnter the row number : ")
                if(r.isdigit()!=True):
                    print("Invalid number entered")
                elif (int(r)<1 or int(r)>9):
                    print("Invalid number entered")
                else:
                    valid=1
            r=int(r)
            
            valid=0
            
            #Continue until valid column input is entered
            while(valid==0):
                c=raw_input("\nEnter the column number : ")
                if(c.isdigit()!=True):
                    print("Invalid number entered")
                elif (int(c)<1 or int(c)>9):
                    print("Invalid number entered")
                else:
                    valid=1
            c=int(c)
            
            #If entry is empty at the entered numberes, then continue, otherwise ask to enter again
            if(arr[r-1][c-1]==0):
                valid_entry=1
                
            else: 
                print('No empty entry at enter row and column number. Try again!')
        
        #Take valid input for number to be filled in sudoku   
        valid=0
        
        #Continue until valid input is entered
        while(valid==0):
            num=raw_input("\nEnter the number to be filled: ")
            if(num.isdigit()!=True):
                print("Invalid number entered")
            elif (int(num)<1 or int(num)>9):
                print("Invalid number entered")
            else:
                valid=1
                
        num = int(num)
        
        #Check if entered number is correct or not
        check=check_input(arr,num,r,c)
        
        #If number is incorrect, terminate, else continue
        if (check==False):
            print("Wrong Number Entered. Please Try Again ! \n")
            break
        print("\nCorrect number entered\n\n")
        print_sudoku(arr)
        
    #If all entries has been successfully filled
    if (i==count-1):
        print("Great! You did it")
        break

