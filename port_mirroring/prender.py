from jinja2 import Template
import yaml
import sys
from glob import glob

datavars_fname = sys.argv[1:1] or glob('*.yml')[0]
template_fname = sys.argv[2:2] or glob('*.j2')[0]

datavars = yaml.load(open(datavars_fname).read())
template = Template(open(template_fname).read())

print template.render(datavars)

