"""Modelos de datos"""
from . import db
import enum


class User(db.Model):
    """Data model para usuarios de la app"""

    __tablename__ = 'app-users'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    username = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )
    email = db.Column(
        db.String(80),
        index=True,
        unique=True,
        nullable=False
    )
    created = db.Column(
        db.DateTime,
        index=False,
        unique=True,
        nullable=False
    )
    admin = db.Column(
        db.Boolean,
        index=False,
        unique=False,
        nullable=False
    )

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
class Gender(enum.Enum):
    female = 'Female'
    male = 'Male'
    non_binary = 'Non binary'

class GenderPref(enum.Enum):
    female = 'Female'
    male = 'Male'
    non_binary = 'Non binary'
    indifferent = 'Indiferent'

class Role(enum.Enum):
    trainer = 'Trainer'
    participant = 'Participant'

class Day(enum.Enum):
    monday = 'Monday',
    tuesday = 'Tuesday',
    wednesday = 'Wednesday',
    thursday = 'Thursday',
    friday = 'Friday'

class Time(enum.Enum):
    shift_1 = '15 to 17h.' ,
    shift_2 = '17 to 19h.',
    shift_3 = '19 to 21h.'

class Place(enum.Enum):
    place_1 = 'Pere Garau',
    place_2 = 'El Terreno',
    place_3 = 'Son Roca',
    place_4 = 'Es Molinar'

class Participant(db.Model):
    __tablename__ = 'participants'
    id_type = db.Column(
        db.String(3)
    )
    id = db.Column(
        db.String(12),
        primary_key=True
    )
    firstname = db.Column(
        db.String(80),
        nullable = False
    )
    lastname = db.Column(
        db.String(100),
        nullable = False
    )
    mail = db.Column(
        db.String(80),
        unique = True,
        nullable = False
    )
    date_birth = db.Column(
        db.Date,
    )
    phone = db.Column(
        db.Integer
    )
    gender = db.Column(
        db.Enum(Gender)
    )
    role = db.Column(
        db.Enum(Role),
        nullable = False
    )
    level = db.Column(
        db.Integer
    )
    practice_place_1 = db.Column(
        db.Enum(Place)
    )
    practice_place_2 = db.Column(
        db.Enum(Place)
    )
    gender_pref = db.Column(
        db.Enum(GenderPref)
    )
    day = db.Column(
        db.Enum(Day)
    )
    time = db.Column(
        db.Enum(Time)
    )
    hobbies = db.Column(
        db.String(130)
    )
    
    class Schedule(db.Model):
        id = db.Column(
            db.Integer,
            primary_key = True
        )
        day = db.Column(
            db.Enum(Day)
        )
        time = db.Column(
            db.Enum(Time)
        )
        practice_place = db.Column(
            db.Enum(Place)
        )
