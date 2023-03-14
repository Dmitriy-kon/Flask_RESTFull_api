from app.dao.genre_dao import GenreDao

from app.servises.genre_service import GenreService

from app.setup_bd import db

# Create Dao
genre_dao = GenreDao(session=db.session)

# Create Services
genre_service = GenreService(dao=genre_dao)
