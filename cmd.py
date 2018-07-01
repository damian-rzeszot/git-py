from sys import argv



def load(name):
    module_name, klass_name = name.split('/', 1)

    module = __import__(module_name, fromlist=[None])
    return getattr(module, klass_name)

def load_command(name):
    return load("git.commands.%s/%sCommand" % (name, name.capitalize()))



try:
    command = argv[1]
except IndexError:
    command = "help"

try:
    klass = load_command(command)
except ModuleNotFoundError:
    print("'%s' is not a command. See 'help'." % argv[1])
    exit(1)


arguments = argv[2:]
repository = None

object = klass(repository)
object.run(*arguments)
