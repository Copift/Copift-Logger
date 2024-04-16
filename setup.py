from setuptools import setup

setup(
   name='Copift-Logger',
   version='1.0',
   description='Copift logger',
   license='MIT',
   author='Sergeev Daniil',
   author_email='danikin000@yandex.ru',
   url='https://github.com/Copift/Copift-Logger',
   packages=['CopiftLogger'],
   install_requires=['sentry-sdk'], # it is empty since we use standard python library
   extras_require={
        'test': [
            'pytest'

        ],
   },
   python_requires='>=3',
)