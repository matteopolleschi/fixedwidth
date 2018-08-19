from setuptools import setup
from path import join, dirname, abspath

basedir = path.abspath(path.dirname(__file__))
with open(path.join(basedir, 'README'), encoding='utf-8') as f:
    long_description = f.read()

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
