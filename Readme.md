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
  commands:
  - command: landing
    is_folder: true
    commands:
    - command: git reset --hard
    - command: git checkout master
    - command: git pull
    - command: npm i
    - command: npm run build
```
### Ejecución 🔧

```
$ python3 main.py
```

![alt text](https://raw.githubusercontent.com/abelhOrihuela/tasks-spark/master/screen1.png)
