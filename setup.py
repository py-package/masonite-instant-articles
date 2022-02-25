from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='masonite-instant-article',
    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.0.7',
    packages=[
        'instant_article',
        'instant_article.config',
        'instant_article.controllers',
        'instant_article.interfaces',
        'instant_article.models',
        'instant_article.providers',
        'instant_article.routes',
        'instant_article.templates',
    ],
    package_dir={"": "src"},
    description='Instant Article for Masonite',
    long_description=long_description,
    long_description_content_type="text/markdown",
    # The project's main homepage.
    url="https://github.com/yubarajshrestha/masonite-instant-articles",
    # Author details
    author='Yubaraj Shrestha',
    author_email='companion.krish@outlook.com',
    # Choose your license
    license='MIT',
    # If your package should include things you specify in your MANIFEST.in file
    # Use this option if your package needs to include files that are not python files
    # like html templates or css files
    include_package_data=True,
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Masonite",

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        'Operating System :: OS Independent',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',

        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=["masonite>=4.0<5.0"],
    # What does your project relate to?
    keywords='masonite, instant articles, development, package',
    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    # $ pip install your-package[dev,test]
    extras_require={
        "dev": [
            "black",
            "flake8",
            "coverage",
            "pytest",
            "pytest-cov",
            "twine>=1.5.0",
            "wheel",
        ],
    },
    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        'templates/index.html': [],
    },
)