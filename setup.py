from setuptools import setup

setup(
    name='httpfs',
    py_modules=['httpfs', 'httpfs_server', 'httpfs_helper_functions', 'file_handling', 'HTTPException', 'logger_init'],
    install_requires=[
        'docopt',
        'portalocker'
    ],
    entry_points='''
        [console_scripts]
        httpfs=httpfs:run
    ''',
)
