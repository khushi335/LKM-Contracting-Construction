import sys
import os

# Add your project directory to sys.path
project_home = "/home/hightech/project22.quantumcoresoftware.com/home"
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Activate virtual environment
venv_path = "/home/hightech/virtualenv/project22.quantumcoresoftware.com/home/3.10"
activate_this = os.path.join(venv_path, "bin", "activate_this.py")

with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Set Django settings module
# Replace 'home.settings' if your Django project folder name is different
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "home.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()