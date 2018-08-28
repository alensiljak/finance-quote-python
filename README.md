# finance-quote-python

Finance::Quote implemented in Python

The idea for this project is to implement the [Finance::Quote](https://github.com/finance-quote/finance-quote) in Python and make it available to other Python code as a library.

## Development

Register the module with `pip install -e .` from the rood directory.

## Distribution

The new way of distributing packages is wia twine. Install: twine, keyring.
Configure [keyring support](https://twine.readthedocs.io/en/latest/#keyring-support).

Package the distribution: `python3 setup.py sdist bdist_wheel`.

Deploy to test: `twine upload -u <username> --repository-url https://test.pypi.org/legacy/ dist/*`

Deploy to Prod: `twine upload -u <username> --repository-url https://upload.pypi.org/legacy/ dist/*`
