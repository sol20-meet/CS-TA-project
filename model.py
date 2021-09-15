from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
Base = declarative_base()

class Place(Base):
	__tablename__ ="Places"
	id = Column(Integer,primary_key=True)
	name_of_place = Column(String)
	description = Column(String)
	user = Column(String)
	imglink = Column(String)
	def __repr__(self):
		return("Place: {}\n"
				"Description: {}\n"
				"User : {}\n"
				"Link :").format(
				self.name_of_place,
				self.descriptions,
				self.user,
				self.imglink)
			