'''Implement a group_by_owners function that:
·         Accepts a dictionary containing the file owner name for each file name.
·         Returns a dictionary containing a list of file names for each owner name, in any order.
For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.'''


def group_by_owners(input):
    result = {}
    for key, value in input.items():
        result[value] = result.get(value, []) + [key]
    return result


input = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}

print(group_by_owners(input))

# output: {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}
