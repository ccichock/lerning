import re


def is_new_tag(line):
    return re.match('<(.+)>', line)


def align_new_tag(line, indent, indent_level):
    indent_level += 1
    for i in range(1, indent_level):
        line = indent + line
    return line, indent_level


def is_single_line(line):
    single_line = re.match('<.+>?.+</.+>', line)
    if single_line:
        return True
    else:
        new_tag = is_new_tag(line)
        if new_tag and (new_tag.group(1).startswith('input') or new_tag.group(1).startswith('link') or new_tag.group(1).startswith('script')):
            return True
    return False


def align_single_line(line, indent, indent_level):
    indent_level += 1
    for i in range(1, indent_level):
        line = indent + line
    indent_level -= 1
    return line, indent_level


def is_close_tag(line):
    return re.match('</.+>', line)


def align_close_tag(line, indent, indent_level):
    for i in range(1, indent_level):
        line = indent + line
    indent_level -= 1
    return line, indent_level


def align(line, indent, indent_level):
    if is_single_line(line):
        return align_single_line(line, indent, indent_level)
    elif is_close_tag(line):
        return align_close_tag(line, indent, indent_level)
    elif is_new_tag(line):
        return align_new_tag(line, indent, indent_level)

    return line, indent_level


def align_indentination(html_string, indent='    '):
    lines = html_string.splitlines(keepends=True)

    indent_level = 0
    indented_lines = []
    for line in lines:
        line, indent_level = align(line, indent, indent_level)
        indented_lines.append(line)

    return ''.join(indented_lines)