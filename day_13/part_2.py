from functools import cmp_to_key

class Element:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value
        self.children = []

    def __repr__(self):
        if self.type == 'int':
            return str(self.value)
        else:
            return '[' + ','.join([str(el) for el in self.children]) + ']'

    def compare(self, other):
        if self.type == 'int':
            if other.type == 'int':
                if self.value == other.value:
                    return 0
                return 1 if self.value < other.value else -1;

            elif other.type == 'list':
                new_el = Element('list')
                new_el.children += [self]
                return new_el.compare(other)

        elif self.type == 'list':
            if other.type == 'int':
                new_el = Element('list')
                new_el.children += [other]
                return self.compare(new_el)

            elif other.type == 'list':
                len_self = len(self.children)
                len_othr = len(other.children)
                for i in range(min(len_self, len_othr)):
                    value = self.children[i].compare(other.children[i])
                    if value in [1, -1]:
                        return value
                if len_self == len_othr:
                    return 0
                return 1 if len_self < len_othr else -1


def parse_line(line):
    token_list = tokens(line)
    return tree(token_list)


def tokens(line):
    i = 0
    tokens = []
    while i < len(line):
        if line[i] in ['[', ']', ',']:
            tokens.append(line[i])
            i += 1
        elif line[i].isnumeric():
            if line[i+1].isnumeric():
                num = int(line[i:i+2])
                i += 1
            else:
                num = int(line[i])
            tokens.append(num)
            i += 1
    return tokens


def tree(tokens):
    if tokens[0] == '[':
        el = Element('list')
        i = 1
        while tokens[i] != ']':
            if isinstance(tokens[i], int):
                sub_el = Element('int', tokens[i])
                el.children.append(sub_el)
                i += 1
            elif tokens[i] == ',':
                i += 1
            elif tokens[i] == '[':
                sub_tree, j = tree(tokens[i:])
                el.children.append(sub_tree)
                i += j
        return (el, i+1)


with open('input.txt') as f:
    lines = f.readlines()
lines += ['[[2]]', '[[6]]']

packets = []
for line in lines:
    if line.strip() != '':
        packets.append(parse_line(line.strip())[0])


def compare_elements(el1, el2):
    return el2.compare(el1)

packets.sort(key=cmp_to_key(compare_elements))
packets_str = [str(s) for s in packets]

t1 = packets_str.index('[[2]]') + 1
t2 = packets_str.index('[[6]]') + 1

print(t1 * t2)

