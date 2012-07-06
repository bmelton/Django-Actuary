from distutils.core import setup

setup(
    name='Django-Actuary',
    version='0.0.2.1dev',
    author='Barry Melton',
    author_email='barry.melton@gmail.com',
    packages=['actuary',], 
    url='http://pypi.python.org/pypi/Django-Actuary/',
    license='LICENSE.txt',
    description='Django auditing application.',
    install_requires=[
        'requests',
    ],
)
