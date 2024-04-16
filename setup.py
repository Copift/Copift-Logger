from setuptools import setup

setup(
   name='Copift-mtracker,
   version='1.0',
   description='Copift test package',
   license='MIT',
   author='Sergeev Daniil',
   author_email='danikin000@yandex.ru',
   url='',
   packages=['mtracker'],
   install_requires=[], # it is empty since we use standard python library
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
)