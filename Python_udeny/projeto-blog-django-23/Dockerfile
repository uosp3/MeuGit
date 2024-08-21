FROM python:3.11.3-alpine3.18
LABEL maintainer="uosp3gs@gmail.com"

# Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instalar dependências necessárias para compilar o mysqlclient
RUN apk add --no-cache \
    mariadb-dev \
    gcc \
    musl-dev \
    libffi-dev \
    build-base \
    python3-dev

# Copia a pasta "djangoapp" e "scripts" para dentro do container.
COPY djangoapp /djangoapp
COPY scripts /scripts

# Entra na pasta djangoapp no container
WORKDIR /djangoapp

# A porta 8000 estará disponível para conexões externas ao container
EXPOSE 8000

# Executa comandos para preparar o ambiente e instalar dependências
RUN python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r /djangoapp/requirements.txt && \
  adduser --disabled-password --no-create-home duser && \
  mkdir -p /data/web/static && \
  mkdir -p /data/web/media && \
  chown -R duser:duser /venv && \
  chown -R duser:duser /data/web/static && \
  chown -R duser:duser /data/web/media && \
  chmod -R 755 /data/web/static && \
  chmod -R 755 /data/web/media && \
  chmod -R +x /scripts

# Adiciona a pasta scripts e venv/bin no $PATH do container
ENV PATH="/scripts:/venv/bin:$PATH"

# Muda o usuário para duser
USER duser

# Executa o arquivo scripts/commands.sh
CMD ["commands.sh"]
