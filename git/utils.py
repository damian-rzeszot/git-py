
def load(name):
    module_name, klass_name = name.split('/', 1)

    module = __import__(module_name, fromlist=[None])

    try:
        return getattr(module, klass_name)
    except AttributeError:
        raise ModuleNotFoundError


def load_command(name):
    try:
        prefix, name = name.split('_', 1)
        return load("git.commands.%s_%s/%s%sCommand" % (prefix, name, prefix.capitalize(), name.capitalize()))
    except ValueError:
        return load("git.commands.%s/%sCommand" % (name, name.capitalize()))


def load_object(name):
    return load("git.objects.%s/%s" % (name, name.capitalize()))
