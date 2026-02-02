from commands import AddCommand, SubCommand
from parser import CommandParser
class CommandInterpreter:
    def __init__(self):
        self.parser=CommandParser()
        self.add_cmd=AddCommand()
        self.sub_cmd=SubCommand()
    def interpret(self, text):
        command, a, b=self.parser.parse(text)
        if command is None:
            return "Invalid command format"
        if command=="add":
            return self.add_cmd.execute(a, b)
        if command=="sub":
            return self.sub_cmd.execute(a, b)
        return "Unknown command"
