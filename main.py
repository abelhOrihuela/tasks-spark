from fabric import Connection
import getpass
import yaml
from helpers import print_color_text, print_log, print_table, run_commands

with open("hosts.yml") as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

hosts = data["hosts"]
print_table(hosts)

selected_host = None
while selected_host is None:
    id_host = int(input("Selecciona el host: "))
    if id_host < len(hosts):
        selected_host = hosts[id_host]
    else:
        print("Host no valido")
password = getpass.getpass("Ingresa la contraseña: ")

try:
    with Connection(
        host=selected_host["host"],
        user=selected_host["user"],
        connect_kwargs={"password": password,},
    ) as c:
        run_commands(c, selected_host)
        print(print_color_text("Done!", 'green'))

except Exception as exception:
    print(TRED + "Error de conexión: ", exception, ENDC)
