from sqlalchemy import *
from sqlalchemy.orm import *
from typing import List

engine = create_engine("mysql+pymysql://#####:######@######:#####/projetim",echo=True)
metadata = MetaData()



class Base(DeclarativeBase):
    pass

class Cliente(Base):
    __tablename__ = "clientes"

    i_ID_clientes:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    s_nome_clientes:Mapped[str] = mapped_column(String(75),nullable=False)
    s_telefone_clientes:Mapped[str] = mapped_column(String(75),nullable=True)

Base.metadata.create_all(engine)

lista1 = []
lista2 = []

print("Coloque os nomes:")

a = 0

while a == 0:
    b = str(input(""))
    if b == "!":
        a = 1
    else:
        lista1.append(b)
a = 0

print("Coloque os nomes:")

while a == 0:
    b = str(input(""))
    if b == "!":
        a = 1
    else:
        lista2.append(b)

while len(lista2) != len(lista1):
    lista2.append('')


for i in range(len(lista1)):
    with engine.connect() as conn:
         aplication = conn.execute(insert(Cliente).values(s_nome_clientes=lista1[i],s_telefone_clientes=lista2[i]))
         conn.commit()


