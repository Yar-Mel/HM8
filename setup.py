from setuptools import setup
setup(
    name='get_birthdays',
    version='0.0.1',
    description='get birthdays on next from list of users',
    url='https://github.com/Yar-Mel/HM8',
    author='Yaroslav Melnychuk',
    author_email='yarmel.dev@gmail.com',
    packages=['get_birthdays'],
    entry_points={'console_scripts': ['get-bd = get_birthdays.get_birthdays:main']}
)