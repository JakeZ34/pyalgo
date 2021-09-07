#1) Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
#Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def change_num(list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list

print(change_num([-1, 3, 5, -5]))

#2) Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
#Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
#Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(list):
    count = 0
    for num in list:
        if num > 0:
            count += 1
    list[len(list) -1] = count
    return list

print(count_positives([-1, 1, 1, 1]))

#3) Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
#Example: sum_total([1,2,3,4]) should return 10
#Example: sum_total([6,3,-2]) should return 7

def sum_total(list):
    sum = 0
    for num in list:
        sum += num
    return sum

print(sum_total([1,2,3,4]))

#4) Average - Create a function that takes a list and returns the average of all the values.
#Example: average([1,2,3,4]) should return 2.5

def average(list):
    count = 0
    for num in list:
        count += num
    return (count) / (len(list))

print(average([1, 2, 3, 4]))

#5) Length - Create a function that takes a list and returns the length of the list.
#Example: length([37,2,1,-9]) should return 4

def length(list):
    return len(list)

print(length([37, 2, 1, -9]))

#6) Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
#Example: minimum([37,2,1,-9]) should return -9

def minimum(list):
    if len(list) == 0:
        return False    
    result = list[0]
    for val in list:
        if val < result:
            result = val
    return result

print(minimum([37, 2, 1, -9]))

#7) 

def maximum(list):
    if len(list) == 0:
        return False    
    result = list[0]
    for val in list:
        if val > result:
            result = val
    return result

print(maximum([37, 2, 1, -9]))

#8) Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
#Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }


def ultimate_analysis(list):
    result = {
        'sum_total': None,
        'maximum': None,
        'minimum': None,
        'average': None,
        'length': 0,
    }
    if len(list) == 0:
        return result
    else:
        result['sum_total'] = 0
        result['maximum'] = list[0]
        result['minimum'] = list[0]
    for val in list:
        if val > result['maximum']:
            result['maximum'] = val
        elif val < result['minimum']:
            result['minimum'] = val
        result['sum_total'] += val
        result['length'] += 1
    result['average'] = result['sum_total'] / len(list)
    return result


print(ultimate_analysis([37, 2, 1, -9]))

#9) Create a function that takes a list and return that list with values reversed. Do this without creating a second list.list

def reverse_list(list):
    half_len = int(len(list) / 2)
    for i in range(half_len):
        list[i], list[len(list) -1 -i] = list[len(list) - 1 - i], list[i]
    return list
print(reverse_list([37, 2, 1, -9]))