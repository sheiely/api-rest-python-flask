from flask import Blueprint
from ..database.config import SessionLocal
from ..controllers import avaliacao_controller as contr

db = SessionLocal()

avaliacoes_routes = Blueprint('avaliacoes', __name__)


avaliacoes_routes.route('/avaliar', methods=["POST"])(contr.avaliar)
