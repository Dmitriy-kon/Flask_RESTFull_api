from app.dao.genre_dao import GenreDao
from app.dao.directors_dao import DirectorDao

from app.servises.genre_service import GenreService
from app.servises.director_service import DirectorService

from app.setup_bd import db

# Create Dao
genre_dao = GenreDao(session=db.session)
director_dao = DirectorDao(session=db.session)

# Create Services
genre_service = GenreService(dao=genre_dao)
director_service = DirectorService(dao=director_dao)
