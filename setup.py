from setuptools import setup, find_packages

setup(
    name='colorman',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'colorama'
    ],
    author='Rishi',
    author_email='technorishi1200@gmail.com',
    description='A package for creating colored boxes in the console',
    url='',
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
