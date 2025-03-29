from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    
    favorites = relationship('Favorite', backref='user', lazy=True)

class Character(Base):
    __tablename__ = 'character'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    gender = Column(String(50))
    birth_year = Column(String(50))
    eye_color = Column(String(50))
    hair_color = Column(String(50))

    favorites = relationship('FavoriteCharacter', backref='character', lazy=True)

class Planet(Base):
    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    climate = Column(String(100))
    terrain = Column(String(100))
    population = Column(String(100))

    favorites = relationship('FavoritePlanet', backref='planet', lazy=True)

class FavoriteCharacter(Base):
    __tablename__ = 'favorite_character'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))

class FavoritePlanet(Base):
    __tablename__ = 'favorite_planet'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))

# Generar el diagrama
try:
    render_er(Base, 'diagram.png')
    print("¡Éxito! Revisa el archivo diagram.png")
except Exception as e:
    print("Error al generar el diagrama:")
    raise e
