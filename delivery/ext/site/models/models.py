from delivery.ext.db import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column("id", db.Integer, primary_key=True)
    email = db.Column("email", db.Unicode, unique=True)
    passwd = db.Column("passwd", db.Unicode)
    admin = db.Column("admin", db.Boolean)
    name = db.Column("name", db.Unicode)
    
    def __repr__(self):
        return self.name
    
class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode, unique=True)
    on_menu = db.Column("on_menu", db.Boolean)
    
    def __repr__(self):
        return self.name
    
class Store(db.Model):
    __tablename__ = 'stores'
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode, unique=True)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("users.id"))
    category_id = db.Column("category_id", db.Integer, db.ForeignKey("categories.id"))
    active = db.Column("active", db.Boolean, default=True)
    
    users = db.relationship("User", foreign_keys=user_id)
    categories = db.relationship("Category", foreign_keys=category_id)
    
class Item(db.Model):
    __tablename__ = "items"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode)
    image = db.Column("image", db.Unicode)
    price = db.Column("price", db.Numeric)
    store_id = db.Column("store_id", db.Integer, db.ForeignKey("stores.id"))
    available = db.Column("available", db.Boolean)
    
    stores = db.relationship("Store", foreign_keys=store_id)
    
class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column("id", db.Integer, primary_key=True)
    created_at = db.Column("created_at", db.DateTime)
    completed = db.Column("completed", db.Boolean)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("users.id"))
    store_id = db.Column("store_id", db.Integer, db.ForeignKey("stores.id"))
    address_id = db.Column("address", db.Integer, db.ForeignKey("address.id"))
    
    users = db.relationship("Users", foreign_keys=user_id)
    stores = db.relationship("Store", foreign_keys=store_id)
    address = db.relationship("Address", foreign_keys=address_id)
    
class OrderItems(db.Model):
    __tablename__ = "order_items"
    id = db.Column("id", db.Integer, primary_key=True)
    order_id = db.Column("order_id", db.Integer, db.ForeignKey("orders.id"))
    items_id = db.Column("items", db.Integer, db.ForeignKey("items.id"))
    qtd = db.Column("qtd", db.Integer)
    
    orders = db.relationship("Order", foreign_keys=order_id)
    items = db.relationship("Item", foreign_keys=items_id)
    
class Checkout(db.Model):
    __tablename__ = "checkouts"
    id = db.Column("id", db.Integer, primary_key=True)
    payment = db.Column("payment", db.Unicode)
    total = db.Column("total", db.Numeric)
    created_at = db.Column("created_at", db.DateTime)
    completed = db.Column("completed", db.Boolean)
    order_id = db.Column("order_id", db.Integer, db.ForeignKey("orders.id"))
    
    orders = db.relationship("Orders", foreign_keys="order_id")
    
class address(db.Model):
    __tablename__ = "address"
    id = db.Column("id", db.Integer, primary_key=True)
    zip = db.Column("zip", db.Unicode)
    country = db.Column("country", db.Unicode)
    address = db.Column("address", db.Unicode)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("users.id"))
    
    users = db.relationship("User", foreign_keys=user_id)