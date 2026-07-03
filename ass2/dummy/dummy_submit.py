import numpy as np
import sklearn

# You are allowed to import any submodules of numpy or sklearn e.g. np.random.randint for random initialization or sklearn.metrics.accuracy_score to calculate accuracy of a learnt model
# You are not allowed to use other libraries such as scipy, keras, tensorflow etc

# SUBMIT YOUR CODE AS A SINGLE PYTHON (.PY) FILE INSIDE A ZIP ARCHIVE
# THE NAME OF THE PYTHON FILE MUST BE submit.py

# DO NOT CHANGE THE NAME OF THE METHODS my_latent, my_latent_updated etc BELOW
# THESE WILL BE INVOKED BY THE EVALUATION SCRIPT. CHANGING THESE NAMES WILL CAUSE EVALUATION FAILURE

# You may define any new functions, variables, classes here

################################
# Non Editable Region Starting #
################################
def my_latent( X, y ):
################################
#  Non Editable Region Ending  #
################################

	z = np.random.randint( 2, size = ( len( y ), ) )
	w = np.zeros( ( X.shape[1] + 1, ) )
	b = 0
	
	return w, b, z

################################
# Non Editable Region Starting #
################################
def my_latent_updated( X, y ):
################################
#  Non Editable Region Ending  #
################################

	w = np.zeros( ( X.shape[1] + 1, ) )
	b = 0
	u = np.zeros( ( X.shape[1], ) )
	a = 0
	
	return w, b, u, a

