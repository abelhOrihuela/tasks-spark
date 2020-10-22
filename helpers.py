from prettytable import PrettyTable
x = PrettyTable()

TYELLOW = "\033[0;33m"  # Green Text
ENDC = "\033[m"  # reset to the defaults
TRED = "\033[92m"

def print_log(step, cm):
    print(TYELLOW + "[" +ENDC+ TRED +"INFO" + ENDC +TYELLOW + "] " + cm + " ==> " + step + ENDC)

def print_color_text(text, color):
    switcher = {
        'red': TRED,
        'green': TRED,
        'yellow': TYELLOW
    }
    return switcher.get(color, TRED) + str(text) + ENDC

def print_table(hosts):
    x.field_names = [
        print_color_text("id", 'yellow'),
        print_color_text("Name", 'yellow'),
        print_color_text("User", 'yellow'),
        print_color_text("Host", 'yellow')
    ]

    i = 0
    while i < len(hosts):
        x.add_row([
            print_color_text(i, 'green'),
            print_color_text(
                hosts[i]["name"], 'green'),
            print_color_text(
                hosts[i]["user"], 'green'
            ),
            print_color_text(
                hosts[i]["host"], 'green'
            )
            ])
        i = i + 1
    print(x)

def run_commands(connection, steps):
    if "steps" in steps.keys():
        for step in steps["steps"]:
            if "cd" in step.keys():
                print_log(step["cd"], 'cd')
                with connection.cd(step["cd"]):
                    run_commands(connection, step)
            else:
                print_log(step["run"], 'run')

                connection.run(step["run"])
                run_commands(connection, step)