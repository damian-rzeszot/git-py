import re



class Config:
    def __init__(self, repository):
        self._repository = repository
        self._sections = self.parse()

    @property
    def repository(self):
        return self._repository

    @property
    def sections(self):
        return self._sections

    def append(self, section):
        self._sections.append(section)

    def save(self):
        content = self.dump()
        self.repository.database.write_file("config", content)

    def parse(self):
        content = self.repository.database.read_file("config")
        parser = Parser()
        return parser.parse(content)

    def dump(self):
        dumper = Dumper()
        return dumper.dump(self)


    def remote_exists(self, name):
        for section in self.sections:
            if (section.name, section.parameters) == ("remote", name):
                return True

        return False





class Dumper:
    def dump(self, config):
        result = "; generated by git-py\n"

        for section in config.sections:
            result += "\n"

            if section.parameters:
                result += "[%s \"%s\"]\n" % (section.name, section.parameters)
            else:
                result += "[%s]\n" % section.name

            for (key, value) in section.entries.items():
                result += "\t%s = %s\n" % (key, value)

        return result





class Parser:

    def parse_section(self, line):
        try:
            r = re.compile('^\[([a-z]+)\]$').match(line)
            return ("section", r[1])
        except TypeError:
            return None

    def parse_section_extra(self, line):
        try:
            r = re.compile('^\[([a-z]+) \"([a-z]+)\"\]$').match(line)
            return ("section_extra", r[1], r[2])
        except TypeError:
            return None

    def parse_entry(self, line):
        try:
            r = re.compile('^([a-z]+) = (.*)$').match(line)
            return ("entry", r[1], r[2])
        except TypeError:
            return None

    def parse_line(self, line):
        methods = [self.parse_section, self.parse_section_extra, self.parse_entry]

        for method in methods:
            r = method(line)
            if r:
                return r

        return None


    def parse(self, content):
        result = []
        section = None

        for line in content.split("\n"):
            line = line.strip()
            match = self.parse_line(line)

            if not match:
                pass
            elif match[0] == "section":
                section = Section(match[1])
                result.append(section)
            elif match[0] == "section_extra":
                section = Section(match[1], match[2])
                result.append(section)
            elif match[0] == "entry":
                section.set(match[1], match[2])
            else:
                print("! config parse error %s" % line)

        return result





class Section:
    def __init__(self, name, parameters = None):
        self._name = name
        self._entries = {}
        self._parameters = parameters

    @property
    def name(self):
        return self._name

    @property
    def parameters(self):
        return self._parameters

    @property
    def entries(self):
        return self._entries

    def set(self, name, value):
        self._entries[name] = value

    def get(self, name):
        return self._entries.get(name)

    def __repr__(self):
        return "<section %s %s>" % (self.name, self.parameters)
