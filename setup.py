from setuptools import setup, find_packages

setup(
    name='HPSocket',
    version='0.9.3',
    packages=find_packages(),
    package_data={'HPSocket': ['*.dll', '*.so']},
    license='MIT',
    author='RonxBulld',
    keywords=("HPSocket", "hpsocket", "HP-Socket", "hp-socket"),
    description = "a python binding for HP-Socket 5.1.1",
    long_description = "a python binding for HP-Socket 5.1.1",
    url='https://gitee.com/RonxBulld/HPSocket4Python',
    platforms = "any",
    zip_safe=False,
    install_requires = []
)
