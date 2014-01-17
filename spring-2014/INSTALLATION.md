# Django installation requirements

Below is a list of the key software you'll need for the advanced data journalism class this semester, along with some resources offering tips about how to get it installed. You'll receive in-class help getting everything up and running during the first couple weeks.

## Python

The main programming language we'll be working in is Python. If you're using a Mac, you should already have it installed. If you're using a PC, you can install it using [this self-installer.](http://www.python.org/ftp/python/2.7.3/python-2.7.3.msi)

**Be sure you install Python 2.6 or 2.7, NOT Python 3.0**

## SQLite

This is the primary database manager we'll be using. Everyone should already have it installed, even if you don't know it. But if you want to be sure, feel free to install [Firefox](http://www.mozilla.org/en-US/firefox/new/). It comes with SQLite included.

## easy_install and pip

To make our lives easier, Python comes with two package management tools, which allow us to install new packages that extend Python's core functionality. You'll probably need some help getting these up and running, but here are some basic instructions:

**On Windows**: http://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows

**On OSX**: easy_install should already be included. To install pip, simply type ```sudo easy_install pip``` and enter your administrative password.

## Various Python packages

Once you install pip, you'll easily be able to install the various Python packages we'll use in class using the command ```pip install LIBRARY-NAME```. If you're on a Mac, be aware that you may have to use the slightly different command ```sudo pip install LIBRARY-NAME```, and then enter your system password, in order to install the software as a superuser.

Libraries we'll be using include:

- [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) for web scraping (```pip install BeautifulSoup```)
- [Mechanize](http://wwwsearch.sourceforge.net/mechanize/), also for web scraping (```pip install mechanize```)
- [Flask](http://flask.pocoo.org/) for web development (```pip install Flask```)
- [Django](http://www.djangoproject.org), also for web development (```pip install django```)

## Github

Github is the primary service most open source programmers use to store and share their code. We'll also be using it to turn in assignments. You'll need to both install the Github client on your local machine and sign up for a free account.

Instructions on getting started can be found here: https://help.github.com/articles/set-up-git
