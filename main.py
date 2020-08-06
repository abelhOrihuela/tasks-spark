from fabric import Connection
import getpass
import yaml

with open('hosts.yml') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

hosts = data["hosts"]

print("============= hosts ===============")
i = 0
while i < len(hosts):
    print("({}): {} - {}@{}".format(i, hosts[i]["name"], hosts[i]["user"], hosts[i]["host"]))
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
    if 'commands' in steps.keys():
        for step in steps["commands"]:
            if 'is_folder' in step.keys() and step["is_folder"]:
                with connection.cd(step["command"]):
                    run_commands(connection, step)
            else:
                connection.run(step["command"])
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
    print("Error de conexión: ", exception)




