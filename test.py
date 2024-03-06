class Customers:
    greeting = "Welcome to the Coffee Palace!"
    pass
customer1 = Customers()
customer1.name = 'Samirah'
customer1.beverage = 'Iced caffe latte'
customer1.food ='Cinnamon Roll'
customer1.total = 225

customer2 = Customers()
customer2.name = 'Jerry'
customer2.beverage = 'Caramel macchiato'
customer2.food = 'Glazed Dougnut'
customer2.total = 230

print(Customers.greeting)
print(customer1.beverage)
print(customer2.food)