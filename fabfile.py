from fabric.api import run, task, get, cd

@task
def deploy_landing():
    with cd('landing'):
        run('git reset --hard')
        run('git checkout master')
        run('git pull')
        run('npm i')
        run('npm run build')
    )

@task
def download_file():
    with cd('/home/app'):
        run('ls -l')
        get(
            local_path='kamino-030720',
            remote_path='kamino-030720'
        )
