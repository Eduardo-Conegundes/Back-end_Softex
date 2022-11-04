import random

def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
                
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        array[j + 1] = key

data = []
for i in range(0, 30):
    data.append(random.randint(1, 1000))
    if data[i] %2 == 1:
        data[i] = data[i]
    else:
        data[i] = data[i] + 1
    
insertionSort(data)
print('Vetor Ordenado:')
print(data)
