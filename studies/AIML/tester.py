map_data = [['A','A','A','A','U','U','U','U'],
['A','A','A','A','U','R','R','R'],
['W','W','W','W','T','T','T','T'],
['W','W','W','W','T','R','R','R'],
['C','C','U','U','T','R','U','U'],
['T','T','T','T','T','T','U','U'],
['U','U','U','U','T','R','U','U']]

def count_type(map_data,map_type):
    count = 0 
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            if map_data[i][j] == map_type:
                count +=1
    return count

res = count_type(map_data,'A')

print(res)

def classify_map(map_data):
    rows=len(map_data)
    cols=len(map_data[0])
    if (count_type(map_data,'R')/(rows*cols))>=0.5:
        print('Suburban')
    elif (count_type(map_data,'A')/(rows*cols))>=0.5:
        print('Farmland')
    elif ((count_type(map_data,'U')+count_type(map_data,'W'))/(rows*cols))>=0.5:
        print('Conservation')
    elif ((((count_type(map_data,'C')/(rows*cols))>=0.5 and ((count_type(map_data,'U')+count_type(map_data,'W'))/(rows*cols))>=0.10) or ((count_type(map_data,'U')+count_type(map_data,'W'))/(rows*cols) <=0.2))):
        print('City')
    else:
        print('Mixed')

classify_map('U')