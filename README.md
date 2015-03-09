Django Bitcoin Penny Auction
============================

BitCoin Penny Auction System built purely in Django.

Getting Started
---------------

I'm assuming you have Python installed and using MAC OSX. It is preferable to have a virtual environment for the project libraries.
Also assuming you've git setup on your system.

Setting Up the Virtual Environment (skip this if you want to mess-up your python libraries :P)
-------------------------------------------------------------------------------------------

If you're using pip to install packages (and I can't see why you wouldn't), you can get both virtualenv and virtualenvwrapper by simply installing the latter.

            pip install virtualenvwrapper

After it's installed, add the following lines to your shell's start-up file (.zshrc, .bashrc, .profile, etc).

            export WORKON_HOME=$HOME/.virtualenvs
            export PROJECT_HOME=$HOME/directory-you-do-development-in
            source /usr/local/bin/virtualenvwrapper.sh

Reload your start up file (e.g. source .bashrc) and you're ready to go.

Creating a virtual environment is simple. Just type

            mkvirtualenv penny

or If already created the Virtual Environment, just start the environment by typing

            workon penny


Getting the App Running
-----------------------

Installing Python Packages and getting the app running is just like eating chocolate.

            cd /path/where/you/want/your/project
            git clone git@bitbucket.org:verdanmahmood/penny-auction.git
            cd penny-auction/
            
Packages can be installed using pip command.
This command installs the packages in the requirement file.
            
            pip install -r requirements.txt
            
Create the Database

            python manage.py syncdb
            python manage.py migrate
            
            
Inserting Test Data, below command will insert the test data. 

            python manage.py insert_test_data

This command will generate an admin user, 4 test users, some and some of the auction items.

Admin User : admin@gmail.com
Admin Pass : 123456

Test User : testuser+1@gmail.com (up to testuser+4@gmail.com)
Test Pass : 123456

Start the Server
            
            python manage.py runserver
            
Once the server is up and running, Open a new terminal tab and make sure to run the following command to run the background process.

            celery -A pennyauction worker -B
            
Accessing Project and Admin
---------------------------

To access the server, please use 

            127.0.0.1:8000
            
To access admin

            127.0.0.1:8000/admin
            
TimeZones
---------

NOTE : ALL THE DATE TIME ARE STORED AND DISPLAYED IN UTC FORMAT.