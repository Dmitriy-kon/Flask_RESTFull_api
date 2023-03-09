### Restfull api на базе flask

- Для работы с бд используется **flask-SQLAlchemy**.
- Используется **marshmallow** для сериализация/десеаризиации.
- Для создания CBV используется **Flask_restx**.

Endpoint для захода в документацию /api

Для GET запроса на api/movies можно использовать query параметры (director_id, genre_id).
Можно использовать по отдельности или вместе.