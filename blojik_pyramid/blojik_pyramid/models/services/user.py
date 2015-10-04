import sqlalchemy as sa

from ..meta import DBSession
from ..user import User


class UserService(object):

    @classmethod
    def by_name(cls, name):
        return DBSession.query(User).filter(User.name == name).first()

    @classmethod
    def get_new_id(cls):
        query = DBSession.query(User).order_by(sa.desc(User.id))
        for q in query:
            new_id = q.id + 1
            break
        return new_id
