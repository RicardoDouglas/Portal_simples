# Dockerfile
FROM python:3.12-slim

# Cria diretório de trabalho
WORKDIR /app

# Copia apenas os arquivos necessários
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Exponha a porta que o Flask usará
EXPOSE 5000

# Comando padrão ao iniciar o container
CMD ["python", "app.py"]
