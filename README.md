# iArticles

[![GitHub stars](https://img.shields.io/github/stars/yubarajshrestha/laravel-module.svg)](https://github.com/yubarajshrestha/iarticles/stargazers)
[![Latest Stable Version](https://poser.pugx.org/yubarajshrestha/iarticles/v/stable)](https://packagist.org/packages/yubarajshrestha/iarticles)
[![Total Downloads](https://poser.pugx.org/yubarajshrestha/iarticles/downloads)](https://packagist.org/packages/yubarajshrestha/iarticles)
[![License](https://poser.pugx.org/yubarajshrestha/iarticles/license)](https://packagist.org/packages/yubarajshrestha/iarticles)

**If you are seeking package for generating instant article or feeds then yes, this package is for you.**

> This helps you generate facebooks instant articles and also regular feeds with enough customizations you might need.

### How to?

#### Step 1: Install package

Install package by executing the command.

```shell
composer require yubarajshrestha/iarticles
```

#### Step 2: Publish Vendor Files

You need to have some files and don't worry it's quite easy. You just want to execute the command now.

```shell
php artisan vendor:publish --tag=iarticles
```

#### Step 3: Update Configurations

You need to define options in your `iarticles` configuration file. You'll find default options from where you will get an idea on how to configure things.

#### Step 4: Implement Instant Article Interface to your Model and configure as follows

```php
use YubarajShrestha\IArticles\InstantArticle;
use YubarajShrestha\IArticles\Articles;
class YourModel implements InstantArticle {


    /**
     * Instant Article
     * @return Collection of YourModel
     */
    public static function getFeedItems()
    {
        return YourModel::latest()->get()->take(25);
    }

    /**
     * Filter Feed Data
     * @return iArticle Object
     */
    public function iArticle()
    {
        return Articles::create([
            'id' => $this->id, // required | integer
            'title' => $this->name, // required | string
            'subtitle' => '', // nullable | string
            'kicker' => $this->kicker, // nullable | string
            'summary' => '', // required | string
            'description' => '', // required | string
            'cover' => '', // nullable | string
            'updated' => '', // required | date
            'published' => Carbon::parse($this->created_at), // required | date
            'link' => '', // full url to item...
            'author' => '' // nullable | email | string
        ]);
    }
}
```

#### Step 5: Awesome

1. Your project is now ready to go :+1:.
