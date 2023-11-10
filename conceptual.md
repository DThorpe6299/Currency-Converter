- ### Conceptual Exercise

    

  Answer the following questions below:

    

  - What are important differences between Python and JavaScript? JavaScript is a coding language meant for frontend use. It can be found in the browser and is very useful on the client-side. Python is a coding language meant for use on the backend. It is used for server side operations and cannot be found in the browser like JavaScript.

    

  - Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you

  can try to get a missing key (like "c") *without* your programming

  crashing.

  1.  my_dict = {"a": 1, "b": 2}
        value = my_dict.get("c", "Key not found")
        print(value)
    2.  my_dict = {"a": 1, "b": 2}
        try:

      value = my_dict["c"]
      print(value)

  except KeyError:
      print("Key not found")

  

    

  - What is a unit test? A unit test is a test done to observe isolated small pieces of code to see if the individual component works.

    

  - What is an integration test? Program units are combined and tested as groups in multiple ways.

    

  - What is the role of web application framework, like Flask? In summary, web application frameworks provide a structured and efficient way to develop web applications by offering abstractions, tools, and conventions. They help streamline the development process, enforce best practices, and contribute to the overall maintainability and scalability of web projects.

    

  - You can pass information to Flask either as a parameter in a route URL

  (like '/foods/pretzel') or using a URL query param (like

  'foods?type=pretzel'). How might you choose which one is a better fit

  for an application? For simple scenarios where the parameters directly represent a resource, route parameters may be more straightforward. For complex filtering, sorting, or dynamic conditions, query parameters offer more flexibility.

    

  - How do you collect data from a URL placeholder parameter using Flask? In Flask, you can collect data from URL placeholder parameters using route patterns. URL placeholder parameters are parts of the URL that are marked by < and > and act as variable placeholders. You can extract these values in your route functions.

    

  - How do you collect data from the query string using Flask? In Flask, you can collect data from the query string using the request object, specifically the request.args attribute. The query string is the part of a URL that follows the "?" character and contains key-value pairs.

    

  - How do you collect data from the body of the request using Flask? Using the request object from Flask. In Flask, you can collect data from the body of a request using the request object. The request object provides access to the data sent in the request, and you can extract information from the request body based on the content type of the request.

    

  - What is a cookie and what kinds of things are they commonly used for? A cookie is a small piece of data that a web server sends to a user's web browser. The browser may store it and send it back with subsequent requests to the same server. Cookies are commonly used for various purposes in web development.

    

  - What is the session object in Flask? a session object is used to track the session data which is a dictionary object that contains a key-value pair of the session variables and their associated values.

    

  - What does Flask's `jsonify()` do? `jsonify()` is a function provided by the Flask web framework for easily converting Python objects into JSON-formatted responses. It's commonly used in Flask routes to return JSON responses from the server. The primary purpose of `jsonify()` is to simplify the process of creating JSON responses and ensure proper handling of JSON encoding.
