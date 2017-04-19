'''
Use this python file to add data to the db as a starting point for our app
'''

from project import db
from project.models import Recipe
from project.models import User

'''
db.create_all eventually calls db.Model.metadata.create_all
Classes are only defined when the modules containing them are imported.
Therefore, if you have a module `my_models` written somewhere, but it is never imported, its code never executes so the models are never registered.

Order of things:
1. Module containing models is imported and executed
2. Model class definition is executed, subclasses, db.Model
3. Model's table is registered with db.Model.metadata
'''
# create the database and the database table
db.create_all()

'''
The following is basically seed data:
'''
# insert recipe data
recipe1 = Recipe('Slow-Cooker Tacos', 'Delicious ground beef that has been simmering in taco seasoning and sauce.  Perfect with hard-shelled tortillas!')
recipe2 = Recipe('Hamburgers', 'Classic dish elivated with pretzel buns.')
recipe3 = Recipe('Mediterranean Chicken', 'Grilled chicken served with pitas, hummus, and sauted vegetables.')
db.session.add(recipe1)
db.session.add(recipe2)
db.session.add(recipe3)

# insert user data
user1 = User('s@s.s', 'ssssss')
user2 = User('p@p.p', 'pppppp')
user3 = User('y@y.y', 'yyyyyy')
db.session.add(user1)
db.session.add(user2)
db.session.add(user3)

# commit the changes
db.session.commit()
'''
End seed data
'''
