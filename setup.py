from setuptools import setup

setup(
    name='pyIMPPN',
    version='0.0.1',
    description='TeamSystem Multi line generator (fixed width)',
    packages=['pyimppn'],
    install_requires=['fixedwidth'],
    license='BSD',
    url='https://github.com/matteopolleschi/pyIMPPN',
    author='Matteo Polleschi',
    author_email='nomail@matteopolleschi.com',
    zip_safe=False,
    keywords='IMPPN TeamSystem',
    test_suite="pyIMPPN.tests",
)
