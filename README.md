# Instant Articles

<p align="center">
    <img src="https://banners.beyondco.de/Masonite%20Instant%20Article.png?theme=light&packageManager=pip+install&packageName=masonite-instant-article&pattern=charlieBrown&style=style_2&description=generate%20facebooks%20instant%20articles%20and%20feeds.&md=1&showWatermark=1&fontSize=100px&images=adjustments&widths=50&heights=50">
</p>

<p align="center">
  
  <img alt="GitHub Workflow Status" src="https://github.com/yubarajshrestha/masonite-instant-articles/actions/workflows/python-package.yml/badge.svg">
  <img alt="PyPI" src="https://img.shields.io/pypi/v/masonite-instant-article">
  <img src="https://img.shields.io/badge/python-3.7+-blue.svg" alt="Python Version">
  <img alt="GitHub release (latest by date including pre-releases)" src="https://img.shields.io/github/v/release/yubarajshrestha/masonite-instant-articles">
  <img alt="License" src="https://img.shields.io/github/license/yubarajshrestha/masonite-instant-articles">
  <a href="https://github.com/yubarajshrestha/masonite-instant-article/stargazers"><img alt="star" src="https://img.shields.io/github/stars/yubarajshrestha/masonite-instant-articles" /></a>
  <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

**If you are seeking package for generating instant article or feeds in Masonite then yes, this package is for you.**

> This helps you generate facebooks instant articles and also regular feeds with enough customizations you might need.

## Installation

```shell
pip install masonite-instant-article
```

## Configuration

Add `InstantArticleProvider` to your project in `config/providers.py`:

```python
# config/providers.py
# ...
from instant_article.providers import InstantArticleProvider

# ...
PROVIDERS = [
    # ...
    # Third Party Providers
    InstantArticleProvider
    # ...
]
```

Then you can publish the configuration by doing:

```bash
python craft package:publish instant_article
```

## Update Configurations

You need to define options in your `instant_article` configuration file inside `config` directory.

```python
# config
INSTANT_ARTICLE = {
    "force_validate": False,
    "feed_details": {
        "your-custom-route-name.xml": {
            'model': 'path-to-your-model-class',
            'title': '',
            'description': '',
            'lang': 'en-us',
            'brand': '',
            'type': 'instant-article' # feed, instant-article
        }
    }
}

# Example
INSTANT_ARTICLE = {
    "force_validate": False,
    "feed_details": {
        "blogs-rss.xml": {
            'model': 'app.models.Blog',
            'title': 'Blog Feed',
            'description': '',
            'lang': 'en-us',
            'brand': '',
            'type': 'instant-article' # feed, instant-article
        },
        "news-rss.xml": {
            'model': 'app.models.News',
            'title': 'News Feed',
            'description': '',
            'lang': 'en-us',
            'brand': '',
            'type': 'instant-article' # feed, instant-article
        }
    }
}

# Above feeds can be access from:
"""
https://your-domain.com/rss/blogs-rss.xml
https://your-domain.com/rss/news-rss.xml
"""
```

## Implementation

```python
from instant_article.interfaces.instant_article_interface import InstantArticleInterface
from instant_article.models.instant_article import InstantArticle


class YourModel(Model, InstantArticleInterface):


    @staticmethod
    def get_feed_items():
        return YourModel.all() # can be any query returning proper values

    def format_feed(self):
        return InstantArticle.create({
            'id': self.id, # required | integer
            'title': self.name, # required | string
            'subtitle': '', # nullable | string
            'kicker': '', # nullable | string
            'summary': '', # required | string
            'description': '', # required | string
            'cover': '', # nullable | string
            'updated': self.updated_at, # required | date
            'published': self.created_at, # required | date
            'link': '', # full url to item...
            'author': '' # nullable | email | string
        })
```

Your project is now ready to go :+1:.

## Contributing

Please read the [Contributing Documentation](CONTRIBUTING.md) here.

## License

masonite-filemanager is open-sourced software licensed under the [MIT license](LICENSE).
