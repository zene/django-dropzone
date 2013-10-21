from fabric.api import *

env.user = "blocmate1"
env.hosts = ["blocmate.com", ]

def start_virtualenv():
    local("workon dropzone")

# Local developent
def start_dev_server():
    local("python manage.py runserver_plus --settings dropzone.settings.dev 0.0.0.0:9000")

def start_dev_shell():
    local("python manage.py shell --settings dropzone.settings.dev")

def start_dev_dbshell():
    local("python manage.py dbshell --settings dropzone.settings.dev")

def run_dev_command(command_name=""):
    """Run a command with the settings thing already setup"""
    local("python manage.py %s --settings dropzone.settings.dev" % command_name)

# Remote serving
def run_prod_command(command_name=""):
    """ Just run this command on remote server """
    with cd("/webapps/django1.5/dropzone_git/dropzone"):
        run("python2.7 manage.py %s --settings dropzone.settings.prod" % command_name)

# def restart_prod_server():
#     """ Start a gunicorn instance using the supervisor daemon from the server """
#     run("sudo supervisorctl restart dropzone")

# Deploy and shit
def deploy(commit="true"):
    if commit == "true":
        local("git add .")
        local("git commit -a")
        local("git push")

    with cd("/webapps/django1.5/dropzone_git"):
        run("git pull")

    with cd("/webapps/django1.5/dropzone_git/dropzone"):
        run("python2.7 manage.py migrate --settings dropzone.settings.prod")
        run("python2.7 manage.py collectstatic --settings dropzone.settings.prod")
    restart_prod_server()
