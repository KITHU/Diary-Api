from .database import db
class ModelOperations(object):
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get(cls, id):
        """
        return entries by id
        """
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_by_email(cls, email):
        """
        return entries by email
        """
        return cls.query.filter_by(email=email).first()
