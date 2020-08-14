# Tasks spark

_Automatización de tareas repetitivas. deploy, backups. etc._

### Paquetes y ambiente 📋

* **Python 3.7**
* **Pipenv**
* **Fabric**
* **Pyyaml**


### Creación de archivo hosts.yml y agregar configuración 🔧

```
hosts:
- host: XX.XX.XX.XX
  name: Landing prod
  user: app
  steps:
  - cd: landing
    steps:
    - run: git reset --hard
    - run: git checkout master
    - run: git pull
    - run: npm i
    - run: npm run build


- host: XX.XX.XX.XX
  name: App Diseño
  user: app
  steps:
  - cd: app-diseno
    folder: true
    steps:
    - run: git pull
    - run: npm i
    - run: npm run prod
  - cd: docker-app-diseno
    steps:
    - run: docker-compose up --build --force-recreate -d
  - run: 'docker exec -i docker-app-diseno_app_1 bash -c
   "cd /var/www/ && php artisan migrate --force"'
```
### Ejecución 🔧

```
$ python3 main.py
```

![alt text](https://raw.githubusercontent.com/abelhOrihuela/tasks-spark/master/screen1.png)
