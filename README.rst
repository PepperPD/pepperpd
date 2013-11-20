------------
PepperPD edX
------------

This package contains customizations to the edX platform made by PepperPD. This
package avoids the pitfalls of simply forking another application and modifying
it and instead overlays new functionality on top of the edX platform and 
modifies existing functionality by overriding URL and template registrations.

Quick Start
===========

The standard development environment is set up in a virtual machine using 
Vagrant.  You'll need at least 5GB of free disk space and you'll need to install
VirtualBox and Vagrant.

- `VirtualBox 4.2 <https://www.virtualbox.org/wiki/Download_Old_Builds_4_2>`_.  
  Other versions may not work correctly with Vagrant.

- `Vagrant <http://www.vagrantup.com/>`_ 1.2.2 or later.

In your development environment::

    $ git clone git@github.com:PepperPD/pepperpd.git
    $ cd pepperpd
    $ vagrant up

Running `vagrant up` for the first time will create a new virtual machine and 
provision the machine to run PepperPD.  To run the services::

    $ vagrant ssh
    $ ./manage.py lms runserver 0.0.0.0:8000
    $ ./manage.py cms runserver 0.0.0.0:8001

The services will run in the foreground, so you'll want to run them in separate
terminal windows or one at a time.  You can visit the LMS at::

    http://192.168.20.40:8000

and the CMS at::

    http://192.160.20.40:8001


