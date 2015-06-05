"""def half_reduce_file_path(path):
    result = ""
    temp = ""
    temp2 = ""
    checkpoint = []
    temp += "/"
    for index in range(0, len(path)):
        if path[index] == "/" and path[index -1] == "/":
            pass
        else:
            temp += path[index]
    for index in range(0, len(temp)):
        if temp[index] == "." and temp[index +1] == "/":
            pass
        elif temp[index] == "/" and temp[index -1] == ".":
            pass
        else:
            temp2 += temp[index]

    return(temp2)
print(half_reduce_file_path("/srv/www/htdocs/../wtf/"))
def reduce_file path(path):
    # [0,4,8,14]
    

print(reduce_file_path("/srv/www/htdocs/../wtf/./"))"""

def kill_char(string, n): 
    begin = string[:n]    
    end = string[n+1:]    
    return begin + end
 
def reduce_file_path(path):
    counter=1
    if path[len(path)-1]=='.':
        path = kill_char(path,len(path)-1)
    if len(path)>1:
        if path[0]=='.' and path[1]!='.':
            path = kill_char(path,len(path)-1)
    while counter < (len(path)-1):
        if len(path)>1 and path[counter]=='.' and path[counter+1]!='.' and path[counter-1]!='.':
            path = kill_char(path,counter)
            counter-=1
        counter+=1        
    counter = 0
    while counter < (len(path)-1):
        if path[counter]=='/' and path[counter]== path[counter+1] and len(path)>2:
            path = kill_char(path,counter+1)
            counter-=1
        counter+=1
        if path[len(path)-1]=='/' and len(path)>1:
            path = kill_char(path,len(path)-1)
    counter=len(path)-1
    counter2=0
    if len(path)>=3:       
        while counter > 0 :
            if path[counter]=='.' and path[counter-1]=='.' and len(path)>3:
                while counter2<2:
                    if path[counter]=='/':
                        counter2+=1
                    path = kill_char(path,counter+1)
                    counter-=1
                counter2=0
                counter=len(path)-1
            counter-=1
    if len(path)==3 and path[2]=='.' and path[1]=='.':
        path = kill_char(path,2)
        path = kill_char(path,1)
                              
    return path
 

print (reduce_file_path("/asf/./adaff/../sd/.////"))

