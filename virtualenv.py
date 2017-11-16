# create a new virtualenv
virtualenv python2

# define which verion of python we will use
virtualenv -p /usr/bin/python3 python3

# Activate the python3 virtualenv.
source python3/bin/activate

# check which packages are installed
pip freeze

# Deactivate the virtualenv.
deactivate
