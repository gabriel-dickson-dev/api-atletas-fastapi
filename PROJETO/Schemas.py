from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class AtletaCreate(BaseModel):
    nome: str = Field(..., max_length=255)
    cpf: str = Field(..., pattern=r"^\d{11}$", description="CPF com 11 dígitos, sem pontuação")
    centro_treinamento: Optional[str] = Field(None, max_length=255)
    categoria: Optional[str] = Field(None, max_length=255)


class AtletaOut(AtletaCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
