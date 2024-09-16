
from flask import Flask, send_from_directory
from .src.models import Usuario
from .src.models import Aluguel
from .src.models import Avaliacao
from .src.models import Filme
from .src.database.config import engine, SessionLocal
from .src.routes.filme_routes import filmes_routes
from .src.routes.aluguel_routes import alugueis_routes
from .src.routes.usuario_routes import usuarios_routes
from .src.routes.avaliacao_routes import avaliacoes_routes
from flask_swagger_ui import get_swaggerui_blueprint


def create_app():
    app = Flask(__name__)
    Usuario.Base.metadata.create_all(bind=engine)
    Aluguel.Base.metadata.create_all(bind=engine)
    Avaliacao.Base.metadata.create_all(bind=engine)
    Filme.Base.metadata.create_all(bind=engine)
    return app


app = create_app()
db = SessionLocal()

app.register_blueprint(filmes_routes, url_prefix='/filmes')
app.register_blueprint(alugueis_routes, url_prefix='/alugueis')
app.register_blueprint(usuarios_routes, url_prefix='/usuarios')
app.register_blueprint(avaliacoes_routes, url_prefix='/avaliacoes')

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Flask Swagger UI"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/static/<path:filename>')
def swagger_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)





