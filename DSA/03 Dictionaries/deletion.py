customer = {'name': 'Prate',
            'mobile': 6786544333,
            'address': 'G-509',
            "date": '27-10-21'}

customer.pop('date') # Deletes provided key value pair and returns value
print(customer)
print(customer.popitem())  # Deletes any random pair
customer.clear()  # Deletes all the elements
print(customer)

# del keyword
owner = {'name': 'Justin', 'mobile': 9888777, 'address': 'G-5011', "date": '27-10-21'}
del owner['date']
print(owner)
