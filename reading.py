import ordering
from daos import Hats
from dtos import Hat, Supplier


def read_and_init(config, repo):
    file = open(config, 'r')
    lines = file.readlines()
    numbers = lines[0].split(',')      
    n_hats = int(numbers[0])            
    n_suppliers = int(numbers[1][:2])   
    for i in range(1, (n_hats + 1)):    
        hat = lines[i].split(',')       
        repo.hats.insert(Hat(int(hat[0]), hat[1], int(hat[2]), int(hat[3][:2])))

    for i in range((n_hats + 1), (n_hats + n_suppliers + 1)):
        word = lines[i].split('\n')
        supplier = word[0].split(',')
        repo.suppliers.insert(Supplier(int(supplier[0]), supplier[1]))


def read_and_order(orders, repo):
    file = open(orders, 'r')
    lines = file.readlines()
    for line in lines:
        word = line.split('\n')
        words = word[0].split(',')
        ordering.order(words[0], words[1], repo)

    orders_output = repo.orders.order_output()
    repo.hats.delete_all_quantity()
    return orders_output


def write_output(output, orders_list):
    file = open(output, 'w')
    for order in orders_list:              
        line = ','.join(order)           
        file.write(line+"\n")

