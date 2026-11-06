import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Por padrão usa SQLite (roda sem configurar nada).
# Para PostgreSQL: export DATABASE_URL="postgresql://user:password@localhost:5432/workout"
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./atletas.db")

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """Dependência do FastAPI: abre e fecha uma sessão por requisição."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
