from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(30))
  phone = db.Column(db.String(30))
  address = db.Column(db.String(120))
  cpf = db.Column(db.String(9))
  
  def serialize(self):
    return {
      'id': self.id,
      'name': self.name,
      'phone': self.phone,
      'address': self.address,
      'cpf': self.cpf,
    }