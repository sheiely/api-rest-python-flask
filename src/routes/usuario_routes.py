from flask import Blueprint
from flask import request, make_response
from ..models.Usuario import Usuario
from ..database.config import SessionLocal
from ..controllers import usuario_controller as contr

db = SessionLocal()
usuarios_routes = Blueprint('usuarios', __name__)

usuarios_routes.route('/criar', methods=["POST"])(contr.criar)
