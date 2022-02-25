from setuptools import setup

setup(
    # Needed to silence warnings
    name='exponents',
    url='https://github.com/rynos1215/python_package_practice',
    author='Evan Rynearson',
    author_email='evan.rynearson@kodares.com',
    # Needed to actually package something
    packages=['exponents'],
    # Needed for dependencies
    #install_requires=['numpy'],
    # *strongly* suggested for sharing
    #version='0.5',
    #license='MIT',
    description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    #long_description=open('README.rst').read(),
    # if there are any scripts
    #scripts=['scripts/hello.py'],
)
