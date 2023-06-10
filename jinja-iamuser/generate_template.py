from jinja2 import Environment, FileSystemLoader


# Define the data to be used in the template
data = {
    'iamusers': ['alaina1', 'alaina2', 'alaina3'],
    'passwords': [1,2,3]
}

# Load the Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
env.globals.update(zip=zip)

# Load the template file
template = env.get_template('template.j2')

# Render the template with the provided data
rendered_template = template.render(data)

# Print the rendered template
print(rendered_template)

# Save the rendered template to a file
output_file = 'rendered_template.yaml'
with open(output_file, 'w') as file:
    file.write(rendered_template)

print(f"Rendered template saved to {output_file}")