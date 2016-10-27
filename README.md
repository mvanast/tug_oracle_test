# tug_oracle_test

A small script and environment to test an oracle db connection

## General Notes

*   Developed using python 3.5, but could be tweaked for other versions, there is nothing required from 3.5
*   The cx-Oracle package to connect with Oracle could be replaced with others, I found this package the easiest to get working however
*   Environment variables used to hide sensitive info (connection string and db sql), use what ever sql you would like to test connection
*   Connection string format: dbuser/password:dns_or_ip:port/DB (eg. my_user/my_nice_passwd:x.x.x.x:1521/my_db_name)
*   This is intented to be setup in a python virtualenv, but you could skip that step if desired 

## Oracle Requirements

Before the cx-Oracle package can be installed, various Oracle drivers need to be installed on the machine running the script. Here are the
general steps i've done. This has been done on Mac OS X, Linux and Windows 10.

helpful reference: http://stackoverflow.com/questions/11245985/easy-install-cx-oracle-python-package-on-windows

1.  Go to the Oracle instant client site: http://www.oracle.com/technetwork/database/features/instant-client/index-097480.html.
2.  Download the rpms (zips for non linux) for your platform, and move to an oracle location to install (eg /usr/local/oracle).

	*	A free Oracle account / login will need  to be created.
	*	Install the 'basic' package first, and don't not use the 'basic-lite', although it
		states its only language packs, other packages won't install if basic-lite was used

3.  I found the linux rpms much easier to use than source install.

4.  install the rpm: (might be handy...: sudo rpm -qa | grep oracle):

    1.  sudo rpm -ivh oracle-instantclient12.1-basic-12.1.0.2.0-1.x86_64.rpm
    2.  sudo rpm -ivh oracle-instantclient12.1-devel-12.1.0.2.0-1.x86_64.rpm
    3.  sudo rpm -ivh oracle-instantclient12.1-jdbc-12.1.0.2.0-1.x86_64.rpm
    4.  sudo rpm -ivh oracle-instantclient12.1-odbc-12.1.0.2.0-1.x86_64.rpm
    5.  sudo rpm -ivh oracle-instantclient12.1-sqlplus-12.1.0.2.0-1.x86_64.rpm
    6.  sudo rpm -ivh oracle-instantclient12.1-tools-12.1.0.2.0-1.x86_64.rpm 
 
5.  Export the path and also add to bash file, ORACLE_HOME very important:
        
    1.  export ORACLE_HOME=/usr/lib/oracle/12.1/client64
    2.  export LD_LIBRARY_PATH=/usr/lib/oracle/12.1/client64/lib
    3.  export PATH=$ORACLE_HOME/bin:$PATH

6.	go to the ORACLE_HOME dir and create some sym links (Linux and Mac):

	1.	sudo ln -s libclntsh.so.12.1 libclntsh.so
	2.	sudo ln -s libocci.so.12.1 libocci.so
	3.	sudo ln -s libslntshcore.so.12.1 libclntshcore.so

## Script environment variables

    1.  setup the connection string in tug_oracle_db: Connection string format: dbuser/password:dns_or_ip:port/DB (eg. my_user/my_nice_passwd:x.x.x.x:1521/my_db_name)
    2.  setup the sql select statement in tug_oracle_sql:

## Python3 and Virtualenv 

Some general helpful linux python3 setup (again this script could easily be converted to python 2.7)
If you're using python 2.7, you'll need to install pip on its own

### system tools and updates

    1.  sudo yum install sqlite sqlite-devel 
    2.  sudo yum install gcc44.x86_64 
    3.  sudo yum install gcc44-c++.x86_64 
    4.  sudo yum install python-devel 

### Python install

1.  The global env must have new version of python available.

        1.  wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz 
        2.  tar zxvf Python-3.5.2.tgz

2.  In the Python3.5.2 dir after unzip:

        1.  ./configure --prefix=/usr/local --with-ensurepip=upgrade --with-gcc=/usr/bin/gcc44 
        2.  make 
        3.  sudo make altinstall 

3.  Adjust .bash_profile, point to new pip and python:

        1.  alias python='/usr/local/bin/python3.5' 
        2.  alias pip='/usr/local/bin/pip3.5' 
        3.  sudo pip3.5 install virtualenv 
        4.  sudo pip3.5 install virtualenvwrapper 

4.  If your virtualenv initailly creates an envirnment with a different python version, you can upgrade:
    *   virtualenv -p python3 <env_name>

## project install 

    1.  In the <env_name> clone the git project: git clone git://github.com/mvanast/tug_oracle_test.git
    2.  cd into tug_oracle_test
    3.  pip install -r requirements.txt
    4.  if cx-Oracle does not install, check the oracle client install
