from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def db_init_app(app):
    global db, migrate

    db.init_app(app)
    with app.app_context():
        db.create_all()


class BaseModel(db.Model):
    __abstract__ = True

    def __str__(self):
        return str(self.json())

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def patch(self, data):
        for field in data:
            if field in self.get_public_field_list():
                setattr(self, field, data[field])
        self.save()
    
    def json(self):
        return {field: getattr(self, field) 
                for field in self.get_public_field_list()}
    
    @classmethod
    def get_public_field_list(cls):
        return [field for field in dir(cls) 
                if not field.startswith('_') and not callable(getattr(cls, field))]    
    
    @classmethod
    def get_by_id(cls, _id):
        return cls.query.get(_id)
