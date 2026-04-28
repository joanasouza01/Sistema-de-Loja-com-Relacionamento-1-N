from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(150))

    Produto = relationship("Produto", back_populates="categorias")

    def __repr__(self):
        return f"categoria = id: {self.id} - nome: {self.nome}"


class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    preco = Column(float, nullable=False)
    estoque = Column(Integer, nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))


    produtos = relationship("Categoria", back_populates="produtos")

    def __repr__(self):
        return f"Produto = id: {self.id} - nome: {self.nome} - preço: {self.preco} - estoque: {self.estoque}"