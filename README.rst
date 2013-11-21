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
provision the machine to run PepperPD.  It may take a while to run the first
time.  To run the services::

    $ vagrant ssh
    $ ./manage.py lms runserver 0.0.0.0:8000
    $ ./manage.py cms runserver 0.0.0.0:8001

The services will run in the foreground, so you'll want to run them in separate
terminal windows or one at a time.  You can visit the LMS at::

    http://192.168.20.40:8000

and the CMS at::

    http://192.160.20.40:8001

Methodology using Git
=====================

A basic agile approach which leverages the strengths of GIT and DVCS is 
recommended for developing PepperPD.  In this scenario all development is split
into narrowly defined, focused units of work which are then implemented on 
individual, single purpose branches.  When work on a branch is complete and has
been verified, it can then be merged to the `master` branch.  `master` is
considered always deployable and should never (knowingly) be put in an
inconsistent or broken state.  The following illustrates the lifecycle a branch
should have.  These steps should be followed in order.

Creating a branch
-----------------

When choosing the scope for a unit of work, choose the smallest scope that makes
sense.  For bug fixes, a fix for a single bug should go on a single branch.  

To create a branch, first make sure you are on master::

    $ git checkout master

Use `git status` to make sure your checkout is clean::

    $ git status
    # On branch master
    nothing to commit (working directory clean)

If the output from `git status` doesn't look exactly like above, do not proceed.
If you're not sure how to get your repository clean, ask for help.  Make sure
you are branching from the most recent commit in `master`::

    $ git pull

Now create a branch.  You guys can decide on the naming convention you'd like to
use for branches.  It is common to include the developer's user name, a 
reference to a ticket in an issue tracker, whether the branch is for a bug or a 
feature, and/or a terse english summary of the changes on the branch::

    $ git checkout -b crossi-493842-bug-registration-email

You now have a branch that you've made off master and ready to do your work.

Working on a branch
-------------------

You should now make the minimum possible changes to implement the work slated 
for your branch.  Run all automated tests before, during and after your work
to make sure you don't introduce any regressions.  Write new tests to make sure
any new code you have written has test coverage.  When the feature works or the
bug has been fixed, all tests pass, and all new code has test coverage, you are
ready to submit your branch to QA.

While working on your branch, you should commit and push early and often.  To 
commit your work, you first add the files you've changed to the commit using
`git add`::

    $ git add <file_or_folder> <file_or_folder>

Use `git status` to see what you are about to commit::

    $ git status

Then use `git commit` to commit your changes::

    $ git commit

Write a terse, but detailed message regarding your commit.  Think in terms of 
what your colleagues will need to know to understand the changes and why you
made them.  Once you're committed, you should push your changes to GitHub.  The
first time you will need to create a remote branch to go with the local branch
you created earlier for your work::

    $ git push -u origin <branch-name>

This creates the remote branch, sets up your local branch to track this remote
branch, and pushes your changes to the remote branch.  Once your local branch
is set up to track the remote branch, pushing is a little easier::

    $ git push

Submit branch to quality assurance (QA)
---------------------------------------

I envision writing a script that can be used to quickly deploy branches for QA.
This script would take a branch name as an argument, spin up a new server in the
cloud (Rackspace, AWS, etc...) and deploy the branch to that server.  Once the
branch is deployed someone other than the developer that did the work on the 
branch should do a quick, focused test only on the functionality which has been
modified on this branch and verify that it either works as expected or needs 
more work.  If the work is rejected, go back to the previous step and start 
again.  If the work is accepted, the branch is eligible to be merged to 
`master`.

As part of the tooling for deploying branches, there will be ways to halt and
restart branch services as well as destroy virtual machines when we are done 
with them.  Obviously, keeping the cloud hosting bill low is a priority so we'll
want to carefully manage how long a branch lives in QA and coordinate having it
up only when testing is under way.

Issue a pull request
--------------------

When a branch passes QA, a pull request should be issued in GitHub signaling 
that the branch is ready to be reviewed by the release manager and merged.  This
is done using the Web UI provided by GitHub.  When viewing the 
`project on GitHub <https://github.com/PepperPD/pepperpd>`_, the last part of
the page header will have a pull down widget that can be used to select a 
branch.  Once the branch is selected, the green button next to the pull down can
be clicked which will open a comparison screen, comparing the code on the branch
to the code on `master`.  From there there will be a prominently displayed link
with the title "Click to create a pull request for this comparison".  Use that
link to create a pull request.

Merge to master
---------------

Someone designated as the "Release Manager" should review pull requests and 
manage merging changes into `master`.  In the beginning stages of development,
it might make sense to have Jazkarta sit as the release manager, while 
the Pepper team learns the basic methodology.  In addition to the testing done
during QA, the release manager should look at the code changed in the pull
request and insure that code conforms to any style guidelines and is of 
sufficiently high quality.  The release manager should insure that new code has
test coverage and that all automated tests pass.  The release manager may ask
the developer to do a little more work if she feels the work doesn't pass 
muster.  Once the release manager approves the branch, the release manager 
merges the branch to master and deletes the branch.  Most of the time, the merge
itself will be seamless, but occasionally the release manager will be required
to fix any merge conflicts.

Once the branch is deployed to `master`, the branch is deployable, since 
`master` is always considered deployable.  

Deployment
==========

In general, organizations which deploy often and routinely, fare better than
organizations that deploy major upgrades only occasionally, as it is more
difficult to manage risk when deployments involve a lot of change and the
organization isn't used to deploying.  Many highly visible organizations use a
continuous deployment model where changes to `master` are automatically deployed
to production.  Other organizations might do deployments once or twice a week
during periods of intense development.  What you want to avoid is deploying 
weeks or months worth of work all in one go.  

What I propose, is the development of a deployment script which automates all
critical aspects of deployment, making deployment routine and easy.  There are
a few technologies currently in use in the Python community: Fabric, Ansible,
etc...  Part of the process would be to choose one.  I envision the deployment 
script will be able to handle provisioning a local Vagrant based development
environment, the QA branch deployments, a preproduction staging environment, and
the production environment, keeping as much the same between these environments
as possible.  Since the same deployment process will be occuring routinely and
constantly at every step and in every environment, we can have high confidence
in its correctness and our understanding of what it's doing.


