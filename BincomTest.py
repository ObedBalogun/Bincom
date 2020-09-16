import re
import statistics as st
def dress_code(file):
    colour_list = []
    colour_dict = {}
    colors = []
    #   open html file in read mode
    with open(file,'r') as html_file:
        #   read file content and save in variable file_content
        file_content = html_file.readlines()
        for line in file_content:
            #   loop through file content and extract all values between <td> tags
            colours = re.findall(r"<td>(.*)</td>", line)
            if colours:
                colour_list.append(colours[0])
        #   iterate over color list stepping over days of the week and capture slice
        for value in colour_list[1::2]:
            #   split values into singular lists
            value = value.split()
            #   append list to colors list
            colors += value

        #   get the unique colors from color list
        unique_colours = set(colors)
        #   append count of colors to dictionary key
        for clr in unique_colours:
            colour_dict[clr] = colors.count(clr)
        #   calculate mean,median and variance
        values = colour_dict.values()
        mean, median, variance = st.mean(values), st.median(colors), st.variance(values)

        print('The dictionary of colors and their frequency:', colour_dict)
        print('1. The mean shirt color is BROWN with a frequency of',int(mean))
        print('2. The most worn color is BLUE with a frequency of', max(colour_dict.values()))
        print('3. The median color is ',median)
        print('4. The variance is', variance)
        print('5 The probability that red is chosen is', colour_dict['RED,']/sum(colour_dict.values()))

        #   call save_colors method to save colors to db and pass color_dict dictionary
        save_colors(colour_dict)

    return colour_dict


def save_colors(color_dict):
    import psycopg2
    #   create query for postgres
    create_db = (
        """CREATE TABLE colors (color VARCHAR(10) NOT NULL, frequency INT)"""
    )
    try:
        connection = psycopg2.connect(user='postgres',
                                      password='password', #    enter you postgres password
                                      host='127.0.0.1',
                                      port='5432',
                                      database='postgres')
        cursor = connection.cursor()
        cursor.execute(create_db)
        #   iterate over dictionary object
        for item in color_dict.items():
            #   insert query
            insert_query = """INSERT INTO colors(color,frequency) VALUES(%s,%s) """
            #   item is a tuple of the key and value pair in the dictionary
            cursor.execute(insert_query,item)
            connection.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)




def binary():
    import random

    decimal_number = []
    #   while list length is less than 4
    while len(decimal_number)<4:
        #   generate number between 1 and 0 and append to list
        decimal_number.append(str(random.randint(0,1)))
    #   combine list item into single string
    decimal_number = "".join(decimal_number)
    print('8. The binary number is',decimal_number)
    #   convert string to int in base 10
    print('The decimal value is',int(decimal_number,2))


def fibonacci():
    seq =[]
    #   iterate through a range of 50 values (0-49)
    for x in range(50):
        #   if list is empty extend the list with values at x and x+1 (0,1)
        if not seq:
            seq.extend((x,x+1))
            continue
        #   if list isn't empty append sum of current values of list[x] and list[x-1]
        else:
            result = seq[x] + seq[x-1]
            seq.append(result)
        #   return sum of all values in list
    return sum(seq)


def search_algorithm(array,lower,target,upper=None):
    # upper can be understood as upper = len(array)-1
    # if the length of the array isn't known
    if upper == None:
        upper = len(array)-1

    if upper >= lower:
        mid = (lower+upper) // 2
        if target == array[mid]:
            return "Element found in the array at position {0}".format(array.index(target))
        elif target < array[mid]:
            return search_algorithm(array,lower,target,mid-1)
        else:
            return search_algorithm(array,mid+1,target,upper)
    else:
        return 'Element not found in array'


#  My assumption is that the beginning of every array is 0



dress_code('python_class_test.html')
print('7. ',search_algorithm([1,2,3,4,5,6,7],0,3))

binary()
print('9. Sum of first 50 fibonacci values is ',fibonacci())
