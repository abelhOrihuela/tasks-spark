from fabric import Connection
import getpass
import yaml
TYELLOW =  '\033[0;33m' # Green Text
ENDC = '\033[m' # reset to the defaults
TRED="\033[0;31m" 

with open('hosts.yml') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

hosts = data["hosts"]

print("============= hosts ===============")
i = 0
while i < len(hosts):
    print(TYELLOW + "{}.- {} - {}@{}".format(i, hosts[i]["name"], hosts[i]["user"], hosts[i]["host"]) + ENDC)
    i+=1

print("===================================")

selected_host = None
while selected_host is None:
    id_host = int(input("Selecciona el host: "))
    if id_host < len(hosts):
        selected_host = hosts[id_host]
    else:
        print("Host no valido")


password = getpass.getpass("Ingresa la contraseña: ")

def run_commands(connection, steps):
    if 'steps' in steps.keys():
        for step in steps["steps"]:
            if 'cd' in step.keys():
                print (TYELLOW + 'cd ===> ' + step["cd"] + ENDC)
                with connection.cd(step["cd"]):
                    run_commands(connection, step)
            else:
                print (TYELLOW + 'run ===> ' + step["run"] + ENDC)
                connection.run(step["run"])
                run_commands(connection, step)


try:
    with Connection(
    host=selected_host["host"],
    user=selected_host["user"],
    connect_kwargs={
        "password": password,
    },
    ) as c:
        run_commands(c, selected_host)
except Exception as exception:
    print(TRED + "Error de conexión: " , exception, ENDC)




