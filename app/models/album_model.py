# Desenvolva sua classe Album abaixo
from platform import release
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from app.configs.database import db
from sqlalchemy.orm import relationship

class Album(db.Model):
    __tablename__ = "albums"

    album_id = Column(Integer, primary_key=True)
    name = Column(String)
    release_date = Column(DateTime)

    band_id = Column(Integer, ForeignKey("bands.band_id"))

    band = relationship("Band", back_populates="albums")
    musics =relationship("Music", backref="album")