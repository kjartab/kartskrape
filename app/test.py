from jinja2 import Environment, FileSystemLoader

template = jinja_environment.get_template('test.html')     
output = template.render(template_values)

with open('test2.html', 'w') as f:
    f.write(output)