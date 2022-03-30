from fastapp.testing import FastAppTestCase
from {{ cookiecutter.project_slug }}.apps import {{ cookiecutter.app_name }}


class Test{{ cookiecutter.app_name }}(FastAppTestCase):
    app_class = {{ cookiecutter.app_name }}
