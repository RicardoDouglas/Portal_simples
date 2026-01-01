# Portal Flask – Um exemplo simples para rodar em Docker
Descrição

Este repositório contém um pequeno portal web construído com Python Flask.

# Estrutura do repositório
.
app.py               # Código da aplicação Flask

Dockerfile           # Instruções para criar a imagem Docker

requirements.txt     # Dependência única: Flask

.gitignore           # Ignora arquivos de build, IDEs, etc.

README.md            # Este documento

# Como rodar localmente (sem Docker)

1. Crie um ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

2. Instale as dependências
pip install -r requirements.txt

3. Inicie a aplicação
python app.py

Acesse http://127.0.0.1:5000 no navegador.


# Como rodar com Docker

1. Build da imagem
docker build -t portal-flask .

2. Executar o container (mapeando a porta 8080 → 5000)
docker run -d -p 8080:5000 --name portal-flask portal-flask

Abra http://localhost:8080 no navegador.


# Para parar e remover o container:
docker rm -f portal-flask




