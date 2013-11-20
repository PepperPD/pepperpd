import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
project = os.path.dirname(os.path.dirname(here))
djangoapps = os.path.join(project, 'pepperpd_lms', 'djangoapps')
sys.path.append(djangoapps)
print 'hi', djangoapps


ROOT_URLCONF = 'pepperpd_lms.urls'
