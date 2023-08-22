#Create a function, which gets some number from text file and returns the average of
#those numbers

def get_average(): #give a name to function
    with open("files\data.txt", "r") as file:
        data = file.readlines() #read mode will give us a text as one single string,
        # but this give us the list

    values = data[1:] # slicing, to cut off 1st
    values = [float(i) for i in values] #store new list in existing variable(values)

    average_local = sum(values) / len(values)
    return average_local


average_local = get_average() #this is a variable which represent a value of the function(get_average)
print(average_local)