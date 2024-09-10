def handler(req, res):
    # Get the query parameters from the URL
    query_params = req.query

    # Create a response message based on query parameters
    if "name" in query_params:
        message = f"Hello, {query_params['name']}!"
    else:
        message = "Hello, stranger!"

    # Set the response status and headers
    res.status_code = 200
    res.headers['Content-Type'] = 'text/plain'
    
    # Send the response
    res.body = message
    return res
