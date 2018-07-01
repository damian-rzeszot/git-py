from sys import argv



def load(name):
    module_name, klass_name = name.split('/', 1)

    module = __import__(module_name, fromlist=[None])
    return getattr(module, klass_name)

def load_command(name):
    return load("git.commands.%s/%sCommand" % (name, name.capitalize()))



klass = load_command(argv[1])
arguments = argv[2:]

repository = None



object = klass(repository)
object.run(*arguments)
