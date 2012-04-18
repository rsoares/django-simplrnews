from setuptools import setup, find_packages


setup(
    name = "django-simplrnews",
    version = "0.1.1",
    packages = find_packages(),
    author = "Ricardo Soares",
    author_email = "ricardo@dengun.com",
    description = "Provides a simple interface to deploy simple article news.",
    url = "http://dengun.com/",
    include_package_data = True,
    zip_safe = True,
)

