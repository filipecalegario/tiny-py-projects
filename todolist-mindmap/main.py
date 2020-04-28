todos = open('todolist.txt').read().split('\n')
output = open('output.md', mode = 'w')

categories = list()

for todo in todos:
    category = todo.split(": ")[0]
    if(category not in categories):
        categories.append(category)
        output.write("# " + category + "\n")
    output.write("## " + todo + "\n")