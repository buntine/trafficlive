from setuptools import setup

setup(name='trafficlive',
      version='0.0.2',
      description='A wrapper of the TrafficLive API',
      url='http://github.com/buntine/trafficlive',
      author='Andrew Buntine',
      author_email='info@bunts.io',
      license='MIT',
      packages=['trafficlive'],
      include_package_data=True,
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
