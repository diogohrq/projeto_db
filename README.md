# Setup inicial

1. Geração da venv:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Instalação dos pacotes:

```bash
pip install -r requirements.txt
```

3. Renomear o .env.example para .env:

```bash
mv .env.example .env
```

4. Rodar o docker-compose:

```bash
# Inicializar
docker-compose up -d

# Finalizar
docker-compose down -v
``` 