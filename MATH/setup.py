from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='mathcalclib',
  version='0.0.1',
  author='Grigoriy Nelyubov',
  author_email='grisha.nelyubov@gmail.com',
  description='Calculate complex impedance and reflection coefficient module',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='-',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='radio math impedance',
  project_urls={
    'GitHub': 'https://github.com/Grishnel/MathCalc.git'
  },
  python_requires='>=3.6'
)