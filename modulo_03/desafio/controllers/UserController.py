from flask import Response, request
from models.User import User, db
import json

def index():
  session = db.session()
  try:
    users = session.query(User).all()
    users_json = [user.serialize() for user in users]
    return Response(json.dumps(users_json))
  except Exception as e:
    session.rollback()
    return {"Error": "Não foi possível listar os usuários!"}
  finally:
    session.close()
    
def store():
  body = request.get_json()
  session = db.session()
  try:
    user = User(name=body['name'],phone=body['phone'],address=body['address'],cpf=body['cpf'])
    session.add(user)
    session.commit()
    return Response(json.dumps([user.serialize()]))
  except Exception as e:
    session.rollback()
    return {"Error": "Não foi possível criar o usuário!"}
  finally:
    session.close()
  
def update(user_id):
  body = request.get_json()
  session = db.session()
  try:
    user = session.query(User).get(user_id)
    
    if body and body['name']:
      user.name = body['name']
    if body and body['phone']:
      user.phone = body['phone']
    if body and body['address']:
      user.address = body['address']
    if body and body['cpf']:
      user.cpf = body['cpf']
      
    session.commit()  
    return Response(json.dumps([user.serialize()]))
  except Exception as e:
    session.rollback()
    return {"Error": "Não foi possível atualizar o usuário!"}
  finally:
    session.close()
  
def show(user_id):
  session = db.session()
  try:
    user = session.query(User).get(user_id)
    return Response(json.dumps([user.serialize()]))
  except Exception as e:
    session.rollback()
    return {"Error": "Não foi possível encontrar o usuário!"}
  finally:
    session.close()
    
def destroy(user_id):
  session = db.session()
  try:
    user = session.query(User).get(user_id)
    session.delete(user)
    session.commit()  
    return {"OK": "Usuário deletado com sucesso!"}
  except Exception as e:
    session.rollback()
    return {"Error": "Não foi possível deletar o usuário!"}
  finally:
    session.close()