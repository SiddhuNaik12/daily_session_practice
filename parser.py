import re
class CommandParser:
    def parse(self, text):
        pattern = r"^(add|sub)\s+(\d+)\s+(\d+)$"
        match = re.match(pattern, text)
        if not match:
            return None, None, None
        command = match.group(1)
        a = int(match.group(2))
        b = int(match.group(3))
        return command, a, b
