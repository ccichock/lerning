

def remove_indent(line):
    while line.startswith('\t') or line.startswith(' '):
        line = line[len('\t'):]
    return line


def remove_indentination(html_string):
    lines = html_string.splitlines(keepends=True)

    indented_lines = [remove_indent(line) for line in lines]
    return ''.join(indented_lines)