import sys
from path import path

# Add our code to the system path
here = path(__file__).dirname()
project = here.dirname().dirname()
lms = project / 'pepperpd_lms'
djangoapps = lms / 'djangoapps'
sys.path.append(djangoapps)

# Use our url config
ROOT_URLCONF = 'pepperpd_lms.urls'

def configure(namespace):
    # Add our templates to the head of the list so they are found first
    templates = lms / 'templates'
    namespace['TEMPLATE_DIRS'].insert(0, templates)
    namespace['MAKO_TEMPLATES']['main'].insert(0, templates)
