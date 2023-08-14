# index-document-app

- src - Code for the application's Lambda function.
- tests - Unit tests for the application code.
- template.yaml - A template that defines the application's AWS resources.

## Deploy the application

To build and deploy your application for the first time, run the following in your shell:

```bash
sam deploy --guided
```

## Tests

Tests are defined in the `tests` folder in this project.
Use pipenv to install the test dependencies and run tests.

```bash
pipenv install --dev
pipenv run test
```

