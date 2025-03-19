import re
from xml.etree import ElementTree as ET

def extract_color_from_scss(scss_file, variable_name):
    with open(scss_file, 'r') as file:
        scss_content = file.read()

    pattern = re.compile(rf'{variable_name}\s*:\s*([^;]+);')
    match = pattern.search(scss_content)

    if match:
        return match.group(1).strip()
    else:
        raise ValueError(f"Variable {variable_name} not found in {scss_file}")

def update_svg_fill_color(svg_file, new_color):
    tree = ET.parse(svg_file)
    root = tree.getroot()

    xmlns = '{http://www.w3.org/2000/svg}'

    for element in root.iter():
        if 'fill' in element.attrib:
            element.attrib['fill'] = new_color

    tree.write(svg_file)

scss_file = '_src/scss/_settings.scss'
variable_name = 'brand-color1'
color_value = extract_color_from_scss(scss_file, variable_name)

svg_files = ['static/img/footer-curve.svg', 'static/img/curve1.svg']
for svg_file in svg_files:
    update_svg_fill_color(svg_file, color_value)

print(f'Successfully updated SVG fill color to {color_value}')
