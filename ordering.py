from dtos import Order

def order(location, topping, repo):                  
    if repo.hats.contains(topping):           
        hat = repo.hats.find(topping)
        hat_id = hat[0]
        if hat_id > 0:
            order_id = repo.orders.size() + 1
            repo.hats.reduce_quantity(hat_id)
            repo.orders.insert(Order(order_id, location, hat_id))




