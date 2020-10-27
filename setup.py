from setuptools import setup

requirements = [
   'requests'
]
setup(
    install_requires=requirements,
    name='this_is_a_package',
    version='2.0',
    packages=['this_is_a_package'],
    author='Vika Po',
    extras_require={
        'dev': [
            'pytest',
            'pytest-pep8',
            'pytest-cov'
        ]
    }
)




# pypi-AgENdGVzdC5weXBpLm9yZwIkNTdlMTI1ZGUtZjZhYy00Y2JjLTkxOTUtYzM4ZGNjM2FjYjkzAAIleyJwZXJtaXNzaW9ucyI6ICJ1c2VyIiwgInZlcnNpb24iOiAxfQAABiDHBpwAoqGPE2K4kK9lP-yjZMI9FI9vv4OfziE6XM6E2Q