.. TODO: Complete the README descriptions and "about" section.


**NOTE: to log in, go to auth/login**


Pokerclubweb Project
========================================


About
-----

This site is for the poker club to track their membership and interact with members and sponsors to organize tournaments and provide club information.

**Unauthorized Capabilites**

- View static information about the club
	- Club mission statement
	- Perks of membership
	- Calendar of upcoming events
	- Current sponsors
	- Poker resources
	- Photo album
	- Exec board
- Sign up for membership (students)
- Contact club about becoming a sponsor
- Home Page have most relevant content (upcoming tournament/event)

**Member Capabilities**

- Register for tournament
- Main tournaments, qualifying tournaments (only tracking information)
- Main tournament: no registration
    - Give instructions for registration for qualifying tournaments:
        - Fill out profile
        - Register with pokerstars league
    - Admin can select 'eligible students'
        - Eligible students can register for main tournament
- Contact me field about becoming an officer
- View tournament results
- Upload personal profile information + resume
- Delete account

**Sponsor Capabilities**

- View current tier of sponsorship
- View student resumes + profiles (based on tier?)
- View tournament results
- Option to upgrade sponsorship?
- Sponsor feed to post messages?

**Admin Capabilites**

- Create tournaments
- Upload tournament results
- Update calendar
- Create sponsor accounts
- Email out to all members

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

Getting dev access on Athena
-----

Find a current admin and have them run the following::

    attach poker
    fs sa /mit/poker [username] all


Now, in your own Athena, run the following to give yourself access rights to the poker locker::

    fs setacl /mit/poker kwlee all


Accessing files on Athena
-----
From Athena, run the following to access the scripts server::

    ssh -k poker@scripts

In a regular terminal, you can run the following instead of ssh-ing from Athena::

    ssh poker@scripts.mit.edu


Notes from Brain
-----

- Website: poker.mit.edu
- Admin: poker.mit.edu/admin (for basic changes like updating BIOs)
- Calendar: Add events to Google Calendar (MIT Poker Club)


To make serious code changes:

1. Login to athena
2. Login to scripts
3. Make changes in local repository, push, and pull in MIT scripts repository.
4. Kill the process associated with the website
    - Go to scripts.mit.edu, scroll to the bottom, and check which server you're connected to.
    - Login to athena, login to that server ($ ssh poker@<>.mit.edu), and kill the associated process (find process in htop and "pkill -9 python" it)

- HTML files corresponding to frontend pages are typically located in /frontend/templates.
- For more complicated issues, you may wish to check views.py, forms.py, and urls.py in different folders.
- For CSS updates, check files corresponding to semantic.min.css.
- To get resumes: run ./compress_resumes.sh, and it should be in ~/web/media/resumes


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
