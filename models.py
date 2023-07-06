from peewee import *

#------------------Database connection------------------
db=SqliteDatabase("Shopyoo.sqlite3")

class Inventory(Model):
    name = CharField(unique=True)
    price = IntegerField()
    quantity=IntegerField()

    class Meta:
        database = db

def create_tables():
    #create tables in sqlite db
    with db:
        db.create_tables([Inventory])


class User_details(Model):
    user_name = CharField(unique=True)
    password= CharField()

    class Meta:
        database = db

def create_tables():
    with db:
        db.create_tables([Inventory,User_details])







        