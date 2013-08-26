from setuptools import setup # pragma: no cover 

setup(name='Synchronise your models with Google Calendar',
      version='0.1',
      py_modules=['djangogcal'],
      cmdclass={'upload':lambda x:None},
      install_requires=[
          'django',
          'gdata',
    ],
)# pragma: no cover 
