import re as regex


class Formater:

    def __init__(self):
        self.one_line_tags = ['input', 'link', 'script']
        self.indent = '    '
        self.indent_level = 0


    def is_new_tag(self, line):
        return regex.match('<(.+)>', line)


    def is_close_tag(self, line):
        return regex.match('</.+>', line)


    def is_one_line_tag(self, line):
        new_tag = self.is_new_tag(line)
        is_one_line_tag = any(new_tag.group(1).startswith(one_line_tag) for one_line_tag in self.one_line_tags)
        return new_tag and is_one_line_tag


    def is_single_line(self, line):
        single_line = regex.match('<.+>?.+</.+>', line)
        return single_line or self.is_one_line_tag(line)


    def add_indent(self, line):
        for _ in range(1, self.indent_level):
            line = self.indent + line
        return line


    def add_indent_new_tag(self, line):
        self.indent_level += 1
        line = self.add_indent(line)
        return line


    def add_indent_single_line(self, line):
        self.indent_level += 1
        line = self.add_indent(line)
        self.indent_level -= 1
        return line


    def add_indent_close_tag(self, line):
        line = self.add_indent(line)
        self.indent_level -= 1
        return line


    def add_indents(self, line):
        try:
            if self.is_single_line(line):
                return self.add_indent_single_line(line)
            elif self.is_close_tag(line):
                return self.add_indent_close_tag(line)
            elif self.is_new_tag(line):
                return self.add_indent_new_tag(line)
            else:
                raise Exception(f'Try to format not html line: {line}')
        except:
            raise Exception(f'Failed to format line: {line}')


    def format_indents(self, html_string):
        lines = html_string.splitlines(keepends=True)

        try:
            indented_lines = [self.add_indents(line) for line in lines]
            return ''.join(indented_lines)
        except Exception as err:
            print (err)
            self.indent_level = 0
            return html_string