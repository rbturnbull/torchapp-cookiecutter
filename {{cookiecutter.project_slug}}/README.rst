================================================================
{{ cookiecutter.project_name }}
================================================================

.. start-badges

|testing badge| |coverage badge| |docs badge| |black badge| |torchapp badge|

.. |testing badge| image:: https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.project_slug }}/actions/workflows/testing.yml/badge.svg
    :target: https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.project_slug }}/actions

.. |docs badge| image:: https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.project_slug }}/actions/workflows/docs.yml/badge.svg
    :target: https://{{ cookiecutter.github_user }}.github.io/{{ cookiecutter.project_slug }}
    
.. |black badge| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    
.. |coverage badge| image:: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/{{ cookiecutter.github_user }}/{{ cookiecutter.coverage_gist }}/raw/coverage-badge.json
    :target: https://{{ cookiecutter.github_user }}.github.io/{{ cookiecutter.project_slug }}/coverage/

.. |torchapp badge| image:: https://img.shields.io/badge/MLOpps-torchapp-B1230A.svg
    :target: https://rbturnbull.github.io/torchapp/
    
.. end-badges

.. start-quickstart

{{ cookiecutter.description }}

Installation
==================================

Install using pip:

.. code-block:: bash

    pip install git+https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.project_slug }}.git


Usage
==================================

See the options for training a model with the command:

.. code-block:: bash

    {{ cookiecutter.project_slug }} train --help

See the options for making inferences with the command:

.. code-block:: bash

    {{ cookiecutter.project_slug }} infer --help

.. end-quickstart


Credits
==================================

.. start-credits

{{ cookiecutter.author_name }}
For more information contact: <{{ cookiecutter.email }}>

Created using torchapp (https://github.com/rbturnbull/torchapp).

.. end-credits

