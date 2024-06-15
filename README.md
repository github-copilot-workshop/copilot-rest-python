## Overview

This project is a Django-based application designed to serve as a learning platform for utilizing GitHub Copilot in software development. The application features a series of labs that guide users through the process of creating API routes, generating sample data, and testing APIs. The project aims to demonstrate the power of GitHub Copilot in streamlining development tasks and enhancing productivity.

## Getting Started
Before diving into the labs, ensure you have Django installed and the project's dependencies are set up. Navigate to the project's root directory and run the following commands:

```bash
cd copilot
python -m pip install -r requirements.txt
```

To start the server, execute:

```bash
python manage.py runserver
```

## Labs Overview

### [Lab 1: Implement New Route](./docs/001-implement-new-route.md)

In this lab, participants will learn how to add a new API route to the Django application. The new route will return a simple "Hello World" JSON response. This lab also includes writing tests for the new route to ensure it behaves as expected.

### [Lab 2: Data and Services](./docs/002-data-and-services.md)

This lab focuses on generating sample data for the application. Participants will create an API that lists Microsoft Azure VMs information, fetched from a local JSON file. This lab covers the entire flow from generating the sample data to testing the new API endpoint.

### [Lab 3: Create Homepage](/docs/003-create-homepage.md)
The details for Lab 3 are not provided in the context. However, based on the naming convention, it's likely focused on creating a homepage for the Django application, possibly involving front-end development aspects and integrating the APIs developed in previous labs.

### Testing

The project includes a suite of tests to validate the functionality of the API routes. To run the tests, ensure the server is not running and execute:

```bash
python manage.py test
```

## Conclusion

This project serves as a practical guide to leveraging GitHub Copilot in developing and testing web applications. Through a series of hands-on labs, participants will gain insights into efficient coding practices and automated testing strategies.

 
