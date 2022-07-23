import pytest

from project.config import config
from project.dao import GenresDAO
from project.models.models import Genre


class TestGenresDAO:

    @pytest.fixture
    def genres_dao(self, db):
        return GenresDAO(db.session)

    @pytest.fixture
    def genre_1(self, db):
        g = Genre(name="Боевик")
        db.session.add(g)
        db.session.commit()
        return g

    @pytest.fixture
    def genre_7(self, db):
        g = Genre(name="Фантастика")
        db.session.add(g)
        db.session.commit()
        return g

    def test_get_genre_by_id(self, genre_1, genres_dao):
        assert genres_dao.get_by_id(genre_1.id) == genre_1

    def test_get_genre_by_id_not_found(self, genres_dao):
        assert not genres_dao.get_by_id(1)

    def test_get_all_genres(self, genres_dao, genre_1, genre_7):
        assert genres_dao.get_all() == [genre_1, genre_7]

    def test_get_genres_by_page(self, app, genres_dao, genre_1, genre_7):
        app.config['ITEMS_PER_PAGE'] = 1
        assert genres_dao.get_all(page=1) == [genre_1]
        assert genres_dao.get_all(page=7) == [genre_7]
        assert genres_dao.get_all(page=10) == []
