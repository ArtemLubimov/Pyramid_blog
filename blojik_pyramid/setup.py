import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid==1.5.7',
    'pyramid_mako', # replaces default chameleon templates
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy==1.0.8',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'wtforms==2.0.2',  # form library
    'webhelpers2==2.0', # various web building related helpers
    'paginate==0.5', # pagination helpers
    'paginate_sqlalchemy==0.2.0'
    ]

setup(name='blojik_pyramid',
      version='0.0',
      description='blojik_pyramid',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='blojik_pyramid',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = blojik_pyramid:main
      [console_scripts]
      initialize_blojik_pyramid_db = blojik_pyramid.scripts.initializedb:main
      """,
      )
