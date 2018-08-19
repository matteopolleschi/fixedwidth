from setuptools import setup
from os.path import join, dirname

f = open(join(dirname(__file__), 'README'))
long_description = f.read().strip()
f.close()

setup(
    name='pyIMPPN',
    version='0.0.1',
    description='TeamSystem Multi line generator (fixed width)',
    packages=['pyimppn'],
    package_dir={'pyimppn': 'pyIMPPN'},
    install_requires=['fixedwidth'],
    license='BSD',
    url='https://github.com/matteopolleschi/pyIMPPN',
    author='Matteo Polleschi',
    author_email='nomail@matteopolleschi.com',
    zip_safe=False,
    keywords='IMPPN TeamSystem',
    test_suite="pyIMPPN.tests",
    long_description=long_description,
    long_description_content_type='text/markdown',
)
