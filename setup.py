from setuptools import setup

setup(name='mcelhaneyhelpers',
      version='0.1',
      description='collection of helper and logger functions',
      url='https://lamplightlab.com',
      author='Matthew McElhaney',
      author_email='matthewmcelhaney@gmail.com',
      license='MIT',
      packages=['mcelhaneyhelpers'],
      install_requires=['datetime', 'json', 'os'],
      zip_safe=False)