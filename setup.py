from setuptools import setup
import re

requirements = []
with open('requirements.txt') as f:
  requirements = f.read().splitlines()



readme = '0.0.1'
with open('README.rst') as f:
    readme = f.read()



setup(name='discord-sb',
      author='AARR-荒らし連合軍',
      url='https://github.com/Rapptz/discord.py',
      version=version,
      packages=packages,
      license='GNU',
      description='A Python wrapper for the selfbot in Discord API',
      long_description=readme,
      long_description_content_type="text/x-rst",
      include_package_data=True,
      install_requires=requirements,
      extras_require=extras_require,
      python_requires='>=3.8.0'
)
