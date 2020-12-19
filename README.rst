Create Pulumi project and stack
-------------------------------

.. code-block:: bash

   export AWS_PROFILE=pasmen
   pulumi login --cloud-url s3://pulumi.linhart.tech
   pulumi new aws-python --dir infra

Provide these values:

- *project name*: pulumi-github-actions
- *project description*: Deploy static website to AWS S3 using Pulumi and GitHub Actions
- *stack name*: pulumi-github-actions-prod
- *passphrase*: <secret-passphrase>
- *aws:region*: eu-central-1

.. code-block:: bash

   export PULUMI_CONFIG_PASSPHRASE=<secret-passphrase>
   cd infra
   pulumi config set aws:profile pasmen

Create website content
----------------------

Create the website content and put it in ``www`` directory.

Modify Pulumi program
---------------------

Modify the Pulumi program in ``infra/__main__.py``.

Preview stack
-------------

Preview stack's resources::

   cd infra
   pulumi preview

Resources
---------

- https://github.com/pulumi/examples/tree/master/aws-py-s3-folder
- https://www.pulumi.com/docs/guides/continuous-delivery/github-actions
