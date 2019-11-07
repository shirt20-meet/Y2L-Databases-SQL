from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
Class Product(Base):
	__tablename__ = 'Product'
	id = Column(Integer, primary_key=True)
	Name = Column(String)
	Price = Column(Float)
	Picture_link = Column(String)
	Description = Column(String)


Class Cart(Base):
	__tablename__ = 'Cart'
	id = Column(Integer, primary_key=True)
	ProductID = Column(Integer)

			
