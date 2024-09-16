from flask import Blueprint
from flask import request, make_response
from ..models.Aluguel import Aluguel
from ..database.config import SessionLocal
from ..controllers import aluguel_controller as contr

db = SessionLocal()

alugueis_routes = Blueprint('alugueis', __name__)


alugueis_routes.route('/criar', methods=["POST"])(contr.criar)

alugueis_routes.route('/listarPorUsuario/<usuario_id>', methods=["GET"])(contr.listarPorUsuario)

