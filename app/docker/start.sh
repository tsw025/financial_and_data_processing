python -m alembic.config upgrade head
uvicorn --host=0.0.0.0 --port=8000 main:app
