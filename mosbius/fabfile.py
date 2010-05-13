from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

def deploy(revision=''):
    if revision!='':
        print "Deploying to server using revision: %s" % revision
    
    updateSource(revision)
    migrateDatabase()
    restartApache()
    
    
def backupDatabase():
    """ Make a backup copy of the database just in a migration fails """
    with cd('~/backups'):
        run('./mosbius.sh')
    
def migrateDatabase():
    
    backupDatabase()
    # In fabric 1.0 we can use the "prefix" context manager instead of 
    # concatenating commands to run in a virtual environment
    with cd('~/webapps/mosbius_website/mosbius/mosbius'):
        run('workon mosbius && python manage.py migrate')

def updateSource(revision=''):
    with cd('~/webapps/mosbius_website/mosbius/'):
        run('hg pull http://www.bitbucket.org/dih0658/mosbius/')
        if revision == '':
            run('hg update')
        else:
            run('hg update -r %s' % revision)
            
def updateDependencies():
    with cd('~/webapps/mosbius_website/mosbius'):
        run('workon mosbius && pip install -U -r requirements.txt')
            
def restartApache():
    run('touch ~/webapps/mosbius_website/mosbius/mosbius/mosbius.wsgi')
    