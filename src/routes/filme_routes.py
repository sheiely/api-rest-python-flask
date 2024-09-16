from flask import Blueprint
from ..database.config import SessionLocal
from ..controllers import filme_controller as contr

db = SessionLocal()

filmes_routes = Blueprint('filmes', __name__)


filmes_routes.route('/criar', methods=["POST"])(contr.criar)

    
filmes_routes.route('/listarPorGenero/<genero>', methods=["GET"])(contr.listarPorGenero)


filmes_routes.route('/buscar/<id>', methods=["GET"])(contr.buscar)
