import unittest
import transaction

from pyramid import testing

from .models.meta import DBSession
from .models import User


class TestMyViewSuccessCondition(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        from .models.meta import (
            Base,
            )
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)
        ''' with transaction.manager:
            model = MyModel(name='one', value=55)
            DBSession.add(model)'''
        with transaction.manager:
            admin = User(name=u'admin', password=u'admin')
            DBSession.add(admin)


    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def test_passing_view(self):
        from .views import my_view
        request = testing.DummyRequest()
        info = my_view(request)
        self.assertEqual(info['one'].name, 'one')
        self.assertEqual(info['project'], 'blojik_pyramid')


class TestMyViewFailureCondition(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        from .models.meta import (
            Base,
            )
        DBSession.configure(bind=engine)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def test_failing_view(self):
        from .views import my_view
        request = testing.DummyRequest()
        info = my_view(request)
        self.assertEqual(info.status_int, 500)