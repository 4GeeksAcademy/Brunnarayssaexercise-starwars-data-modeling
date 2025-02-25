from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from datetime import datetime

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    fecha_suscripcion = db.Column(db.DateTime, default=datetime.utcnow)

    favoritos = relationship('Favorito', back_populates='usuario', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Usuario {self.nombre} {self.apellido}>'

class Personaje(db.Model):
    __tablename__ = 'personaje'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    imagen = db.Column(db.String(250), nullable=True)

    favoritos = relationship('Favorito', back_populates='personaje')

    def __repr__(self):
        return f'<Personaje {self.nombre}>'

class Planeta(db.Model):
    __tablename__ = 'planeta'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    imagen = db.Column(db.String(250), nullable=True)

    favoritos = relationship('Favorito', back_populates='planeta')

    def __repr__(self):
        return f'<Planeta {self.nombre}>'

class Favorito(db.Model):
    __tablename__ = 'favorito'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.Enum('personaje', 'planeta', name='tipo_favorito'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    referencia_id = db.Column(db.Integer, nullable=False)

    usuario = relationship('Usuario', back_populates='favoritos')
    personaje = relationship('Personaje', back_populates='favoritos', foreign_keys=[referencia_id], primaryjoin="and_(Favorito.referencia_id==Personaje.id, Favorito.tipo=='personaje')")
    planeta = relationship('Planeta', back_populates='favoritos', foreign_keys=[referencia_id], primaryjoin="and_(Favorito.referencia_id==Planeta.id, Favorito.tipo=='planeta')")

    def __repr__(self):
        return f'<Favorito {self.tipo} - Referencia ID {self.referencia_id}>'
