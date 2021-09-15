from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
# session = scoped_session(sessionmaker(bind=engine))
DBSession = sessionmaker(bind=engine)
session = DBSession()

#add_place takes 4 variables and it creates an Place Object and then it adds it to the database so it can be accessed later on..
def add_place(place,description,user,link):
	place_obj = Place(
		name_of_place = place,
		description=description,
		user = user,
		imglink = link)
	session.add(place_obj)
	session.commit()


#query_all gets all of the Place objects in the database and it returns them as a list which is called Places
def query_all():
	Places = session.query(Place).all()
	return Places
