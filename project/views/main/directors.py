from flask_restx import Namespace, Resource

from project.container import director_service
from project.setup.api.models import director
from project.setup.api.parsers import page_parser

api = Namespace('directors')


@api.route('/')
class DirectorsView(Resource):
    @api.expect(page_parser)
    @api.marshal_with(director, as_list=True, code=200, description='OK')
    def get(self):
        """
        Получаем всех режиссеров
        """
        return director_service.get_all(**page_parser.parse_args())


@api.route('/<int:director_id>/')
class DirectorView(Resource):
    @api.response(404, 'Not Found')
    @api.marshal_with(director, code=200, description='OK')
    def get(self, director_id: int):
        """
        Получаем режиссера по id
        """
        return director_service.get_item(director_id)
