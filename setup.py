from setuptools import find_packages, setup

setup(name='poker_bot',
      version='0.2',
      description='PokerBot',
      #url='https://github.com/fishbiat/poker-bot',
      author='Fishbiat',
      author_email='none@example.com',
      install_requires=[],
      license='Apache',
      packages=find_packages(exclude=['*.test', '*.tests']),
      #packages=['poker_bot'],
      zip_safe=False)
