import setuptools


with open('README.md', encoding='utf-8') as readme:
    long_description = readme.read()


setuptools.setup(
    name='hozyain_api',
    version='1.0.4',
    author='Nikita Kaner',
    author_email='nikitaKaner@corp.laserpoint.ru',
    description='Package that helps to communicate with the HOZYAIN.API in python',
    long_description=long_description,
    url='https://github.com/Justcleancountry/py_hozyain_api_communicator',
    packages=['hozyain_api_communicator'],
    install_requires=['gql[all]', 'pydantic'],
)
