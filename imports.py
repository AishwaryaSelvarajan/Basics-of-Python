import printing_functions
from printing_functions import print_models
from printing_functions import print_models as pm
import printing_functions as pf
from printing_functions import *

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pm(unprinted_designs, completed_models)
pf.print_models(unprinted_designs, completed_models)
