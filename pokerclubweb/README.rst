.. TODO: Complete the README descriptions and "about" section.

Pokerclubweb Project
========================================

About
-----

Describe your project here.

Prerequisites
-------------

- Python >= 2.6
- pip
- virtualenv (virtualenvwrapper is recommended)

Installation
------------

To setup a local development environment::

    virtualenv env --prompt="(pokerclubweb)"  # or mkvirtualenv pokerclubweb
    source env/bin/activate

    pip install -r requirements.txt
    edit pokerclubweb/settings/project.py    # Enter your DB credentials
    cp pokerclubweb/settings/local.py.example pokerclubweb/settings/local.py  # To enable debugging

    ./manage.py syncdb --migrate
    ./manage.py runserver

Compiling SASS files
~~~~~~~~~~~~~~~~~~~~

Sass files are compiled to CSS during the development.
At the server, there is no need for installing development tools.

To setup your development system, install NodeJS from https://nodejs.org/.
On Mac OSX, you can also use ``brew install libsass node``.

Run the following command to compile SASS_ files::

    npm run gulp

This will compile the files, and watch for changes.
It also has LiveReload_ support.
Install a browser plugin from: http://livereload.com/extensions/
and toggle the "LiveReload" button in the browser to see CSS changes instantly.

License
-------

Describe project license here.


.. Add links here:

.. _django-fluent: http://django-fluent.org/
.. _LiveReload: http://livereload.com/
.. _SASS: http://sass-lang.com/
