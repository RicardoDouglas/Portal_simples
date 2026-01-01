# app.py
from flask import Flask, render_template_string

app = Flask(__name__)

# -------------------------------------------------
# Template base – contém um placeholder {{ content }}
# -------------------------------------------------
HTML_TEMPLATE = """
<!doctype html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8">
    <title>Portal Simples</title>
    <style>
        body {font-family: Arial, sans-serif; margin:0; padding:0;}
        header, footer {background:#004d40; color:#fff; text-align:center; padding:1rem;}
        nav {background:#00695c; padding:0.5rem;}
        nav a {color:#fff; margin:0 1rem; text-decoration:none;}
        main {padding:2rem;}
    </style>
</head>
<body>
    <header>
        <h1>Bem‑vindo ao Portal Simples</h1>
    </header>

    <nav>
        <a href="/">Home</a>
        <a href="/sobre">Sobre</a>
        <a href="/contato">Contato</a>
    </nav>

    <main>
        {{ content | safe }}
    </main>

    <footer>
        © 2026 Portal Simples – desenvolvido por Ricardo
    </footer>
</body>
</html>
"""

# -------------------------------------------------
# Funções auxiliares para gerar o HTML da página
# -------------------------------------------------
def render_page(body_html: str):
    """Renderiza a página inserindo *body_html* no placeholder {{ content }}."""
    return render_template_string(HTML_TEMPLATE, content=body_html)


# -------------------------------------------------
# Rotas
# -------------------------------------------------
@app.route("/")
def home():
    body = "<p>Esta é a página inicial.</p>"
    return render_page(body)


@app.route("/sobre")
def sobre():
    body = (
        "<p>Este portal foi criado como exemplo de implantação em container.</p>"
    )
    return render_page(body)


@app.route("/contato")
def contato():
    body = (
        "<p>Entre em contato: "
        "<a href='mailto:ricardo@example.com'>ricardo@example.com</a></p>"
    )
    return render_page(body)


# -------------------------------------------------
# Execução
# -------------------------------------------------
if __name__ == "__main__":
    # Escuta em todas as interfaces (necessário para Docker)
    app.run(host="0.0.0.0", port=5000, debug=False)   # mantenha debug=False em produção
