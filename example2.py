from example import Customer, CreditCard, Order

from sqlalchemy import func, create_engine, select
from sqlalchemy.orm import Session, Query

# this is an engine
engine = create_engine("sqlite:///my_database.db", echo=True)

# Select customer name with their number of orders
query = select(Customer.id, func.count(Order.id)).join(Order).group_by(Customer.id)


# Querying through a relationship
# Here we use Customer.orders to see if it can return results where customers
# have ordered 2 or more items
# this query threw a AttributeError: Neither 'InstrumentedAttribute' object nor
# 'Comparator' object associated with Customer.orders has an attribute 'quantity'
# query = select(Customer.id,Customer.name,Customer).where(Customer.orders.quantity >=2)

# this worked when inside a session
# has an explicit join
find_atleast_two_items = Query(Customer).join(Order).filter(Order.quantity >= 2)


with Session(engine) as session:
    results = session.execute(find_atleast_two_items).all()

    print(results)
