def read_data(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()

def read_code(file_name):
    with open(file_name, 'r') as file:
        return file.read()

def write_data(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()

def get_md_headline(data):
    return '# ' + data + '\n'

def get_md_head(data):
    return '## ' + data + '\n'

def get_md_anchor(data):
    return '+ [{}](#{})'.format(data, '-'.join(data.split(' ')))

def get_md_link(data):
    return data

def get_md_code_block(solution):
    return '```python\n{}\n```\n'.format(solution)

def get_md_details(title, data):
    return '<details><summary>{}</summary><blockquote>\n\n{}\n</blockquote></details>'.format(title, data) + '\n'

if __name__ == '__main__':
    generator = read_data('generator.txt')
    data = ''
    data = get_md_headline(generator[0]) + '\n'
    data += get_md_anchor(generator[1]) + '\n'
    data += get_md_head(generator[1]) + '\n'
    data += get_md_link(generator[2]) + '\n'

    tests = read_code('test.py')
    data += get_md_details(generator[3], get_md_code_block(tests)) + '\n'

    solution = read_code('solution.py')
    data += get_md_code_block(solution)

    write_data('arrays.md', data)