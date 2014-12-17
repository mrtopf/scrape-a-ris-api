from setuptools import setup, find_packages

version = '0.1'

setup(name='eschweiler-api',
      version=version,
      description="an API for the eschweiler ratsinfo data",
      long_description="""
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='COM.lounge',
      author_email='info@comlounge.net',
      url='',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        "pymongo",
        "mongogogo",
        "starflyer",
      ],
      entry_points="""
      [paste.app_factory]
      main = api.app:app
      """,
      )
