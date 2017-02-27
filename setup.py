from setuptools import setup

setup(
    name='httpfs',
    py_modules=['httpfs', 'httpfs_server'],
    install_requires=[
        'docopt',
    ],
    entry_points='''
        [console_scripts]
        httpfs=httpfs:run
    ''',
)
