FROM python:3.11-slim

WORKDIR /app

# Instalar dependências do sistema necessárias para compilação
RUN apt-get update && apt-get install -y

# Copiar o arquivo de requisitos
COPY requirements.txt /app/

# Instalar as dependências do Projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código-fonte do projeto para o container
COPY . /app/

# Variável de ambiente para evitar buffering nos logs
ENV PYTHONUNBUFFERED=1