student = {'name' : 'Surbhi Kumari', 'age': 24, 'course' : 'DSA', 'Batch' : 2018}

def searching(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return "Value doesn't exist"

print(searching(student, 2018))