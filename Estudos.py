from sqlalchemy import create_engine,text,Column,Integer,String,Table,MetaData,ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase


engine = create_engine('mysql+pymysql://root:itamarati01@localhost:3306/estudos' ,echo=True)
engine2 = create_engine('mysql+pymysql://root:itamarati01@localhost:3306/estudos_orm' ,echo=True)
metadata = MetaData()
with engine.connect() as conn:
    s = conn.execute(text(
        f'''select i_IDprodutos_produtos,s_NomedoProduto_produtos,i_QTD_produtos from produtos where i_IDprodutos_produtos > :y '''),

    for row in s:
        print(f'x:{row.i_IDprodutos_produtos} y:{row.s_NomedoProduto_produtos}')

    conn.commit()

stmt = text('''select i_IDprodutos_produtos,s_NomedoProduto_produtos,i_QTD_produtos from produtos where i_IDprodutos_produtos > :y''')

with Session(engine) as session:
   result = session.execute(stmt, {'y':1})
   for row in result:
        print(f'x:{row.i_IDprodutos_produtos} y:{row.s_NomedoProduto_produtos}')

with engine.connect() as conn:
    a = Table("User",metadata,
              #Column('i_ID_User',Integer,primary_key=True,autoincrement=True),
    Column('s_nomedeusuario_User',String(30),nullable=False),
    Column('s_Senha_User',String(15),nullable=False))

    b = Table('Adresses',metadata,
            Column('i_ID_Adresses',ForeignKey('User.i_ID_User'),nullable=False),
              Column('i_Tipo_Adresses',String(15),nullable=True)
              )
    metadata.create_all(engine)


while True:

    try:
       s = 0
       Inpull1 = str(input('1 = Digite:'))
       Inpull2 = str(input('2 = Digite:'))

       with engine.connect() as cunn:
          p = cunn.execute(text('''INSERT INTO User (s_nomedeusuario_User,s_Senha_User)
          Values (:x, :y)'''),{'x': Inpull1,'y': Inpull2})

          cunn.commit()


       s += 1

       if s == 10:
          #break


    except ValueError:
         print('1 = Tem que ser \n Uma STRING \n 2 = Tem que ser \n Uma STRING ')
         continue

t = input('Digite:')

with engine.connect() as cunn:
    p = cunn.execute(text(f'''SELECT i_ID_User,s_nomedeusuario_User,s_Senha_User From User
    where s_Senha_User = :y '''),{'y': t })

    for row in p:
        print(row)


class Base(DeclarativeBase):
    pass



from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'User'

    i_ID_User:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    s_Nome_User:Mapped[str] = mapped_column(String(15),nullable=False)
    s_Senha_User:Mapped[str] = mapped_column(String(12),nullable=False)

    addresses: Mapped[List["Address"]] = relationship(back_populates="user")

class Address(Base):
    __tablename__ = "address"

    i_id_address: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    email_address: Mapped[str] = mapped_column(String(20))
    user_id_address = mapped_column(ForeignKey("User.i_ID_User"))

    user: Mapped[User] = relationship(back_populates="addresses")

Base.metadata.create_all(engine2)

sa = Table('User',metadata,autoload_with=engine2)











