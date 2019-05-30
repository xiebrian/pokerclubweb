MIT Poker Club Website
======================

This site is for the MIT Poker Club to track their membership, interact with members/sponsors, and display relevant club information.

If you are a MIT Poker Club committee member, please follow the below steps in order to acquire admin access to the website.

Get dev access on Athena
------------------------

Find a current admin and have them run the following::

    attach poker
    fs sa /mit/poker [username] all

Now, in your own Athena, run the following to give yourself access rights to the poker locker::

    fs setacl /mit/poker [your_kerberos] all

This will allow you to ssh into the poker club locker through Athena (which is where the codebase that is being run is stored).

Accessing files on Athena
-------------------------

From Athena, run the following to access the scripts server::

    ssh -k poker@scripts

In a regular terminal, you can run the following instead of ssh-ing from Athena::

    ssh poker@scripts.mit.edu

Making changes to the Database
------------------------------

Website: poker.mit.edu
Admin: poker.mit.edu/admin
Calendar: Add events to the Google Calendar (MIT Poker Club)

Most changes to the database (such as updating admin/sponsor BIOs, fixing member accounts, etc) should be done through the admin interface. 

To make changes to the "upcoming events" section of the website, simply add events to the MIT Poker Club Google Calendar (there should be a guide in the Google Drive). There may be some latency, but it will eventually show up on the website.

Making serious code changes
---------------------------

1. Login to the Poker Club locker as specified above::

    ssh brianxie@athena.dialup.mit.edu
    ssh -k poker@scripts

2. Make desired changes in the pokerclubweb repository. If you would prefer to make changes locally, clone the pokerclubweb repository from my GitHub (https://github.com/xiebrian/pokerclubweb). Commit, push, and pull into the Poker Club locker repository. If you do this however, please try to keep the commit history clean and squash any changes pertaining to the same issue.

3. You'll notice that even if you refresh the Poker Club webpage, the changes will not display. This is because the process that runs the website is using a cached copy of the code. You will need to kill the process associated with the website:

- Go to https://scripts.mit.edu, scroll to the bottom, and check which server you're connected to. This should be something like "You are currently connected to pancake-bunny.mit.edu".
- Log into athena, and log into that specific server. For example::

    ssh brianxie@athena.dialup.mit.edu
    ssh poker@pancake-bunny.mit.edu

- The process associated with the website should have USER 'poker' and the command running should look something like "python index.cfgi". You can kill it by running 'htop' and SIGTERM'ing the process.
- Refresh, and you should be able to see the changes now.

Where should I make changes?
----------------------------

If you are making changes to the static information or the templates, you should most likely look in /frontend/templates. Edit the corresponding HTML files.

If you're looking to make more complicated changes (such as requiring a user-uploaded resume upon account creation), you will want to check views.py, forms.py, urls.py, models.py in different folders. Most likely that folder will be /users. 

If for some reason you want to make changes to the admin interface, that will be in admin.py files across the different folders.

For CSS updates, check the files corresponding to semantic.min.css. There have already been some minor changes to this file.

To get a ZIP file containing all of the resumes, run::
    
    ./compress_resumes.sh

This will compress all the resumes in /web/media/resumes into one file. The resulting file will be /web/media/resumes.tar.gz, which you can transfer to your local machine using scp.

Miscellaneous Information
-------------------------

**Unauthorized Capabilites**

- View static information about the club
	- Club mission statement
	- Calendar of upcoming events
	- Current sponsors
	- Exec/alumni board
    - Contact information and FAQ 
- Sign up for membership (students)
- Contact club about becoming a sponsor

**Member Capabilities**

- Contact me field about becoming an officer
- Upload personal profile information + resume
- Delete account

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
