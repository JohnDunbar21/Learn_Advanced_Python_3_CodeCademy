# Deploying a Simple Python Script with Flask

## What is deployment?

After we have designed, built, and thoroughly tested our application, it is time to package it up and ready it for a production state. This process is called deployment. This allows our application to successfully execute in an environment other than our development and test environments.

There are several methods for deploying applications, but in this article, we will dive into deploying a simple web application to a local server using the Python web framework, Flask.

Flask is a lightweight framework for developing web applications. It provides an efficient and easy way to deploy web-based projects. Flask offers a built-in development server that we can use to test and deploy web application code locally (which we will cover in this article). It also includes useful features like templating that allow us to render HTML templates and provide the functional back-end code for template components

## Understanding the code

Take a look at the following calculator application code. We must first import the Flask library into our application in order to use it later on.

```py
app = Flask(__name__)
 
@app.route('/')
def welcome():
  return "Welcome to the Codecademy Calculator!"
```

Next, we create a Flask instance and assign it to the variable named app. We can create several routes using the `@app.route` decorator.

These routes correspond to the URL web request made to access different pages of the web application. The function that follows the decorator executes upon the web request. The main URL of our application is denoted by `/`. If we want to add additional URL routes for `/division` or `/multiplication`, we can define routes in our Flask application for each.

```py
# allows user to input two numbers
num1 = int(input('Enter your first number: '))
num2 = int(input('Enter your second number: '))
 
@app.route('/division')
def division():
  return "Now dividing " + str(num1) + " and " + str(num2) + "! The result is: {result}".format(result=str(num1/num2))
 
@app.route('/multiplication')
def multiplication():
  return "Now multiplying " + str(num1) + " and " + str(num2) + "! The result is: {result}".format(result=str(num1*num2))
```

Let’s review the following code:

- `num1` and `num2` allow users to input two numbers to multiply or divide.
- `@app.route('/division')` specifies the web request with /division.
- `division()` is a function that executes in the /division route. This function divides the values num1 and num2.
- `@app.route('/multiplication')` specifies the web request with /multiplication.
- `multiplication()` is a function that executes in the /multiplication route. This function multiplies the values num1 and num2.

Finally, we need to add the last line to our program:
```py
app.run()
```
Calling `app.run()` will start the application server allowing the application to load in the web browser.