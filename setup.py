from distutils.core import setup


setup(
    name = "django-userswitch-fork",
    version = "0.2.4",
    packages = ['userswitch',],
    license = "New BSD License",
    author = "iKraft Software (P) LTD. (see AUTHORS.rst)",
    author_email = "hello@ikraftsoft.com",
    maintainer = "Sumit Chachra",
    maintainer_email = "sumit@tivix.com",
    description = "A quick 'n' dirty Django app for switching between different users while testing",
    long_description=open('README.rst').read(),
    url = "https://github.com/ikraftsoft/django-userswitch",
    download_url="https://github.com/ikraftsoft/django-userswitch/tarball/master",
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
