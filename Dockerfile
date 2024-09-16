FROM python:3-alpine

WORKDIR /app

COPY requirements.txt .

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

COPY . .




# Expor a porta que o Flask irá rodar (porta 5000 por padrão)
EXPOSE 5000

# Definir as variáveis de ambiente

# Rodar o comando para iniciar a aplicação
ENV FLASK_APP=app.py

# Comando para rodar o Flask quando o container iniciar
CMD ["flask", "run", "--host=0.0.0.0"]