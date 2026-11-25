from views import create_request, get_requests, update_request_status

request_data = {
    "title": "Laptop Request",
    "description": "Need a new laptop for development work"
}

print(create_request(request_data))
print(get_requests())

print(update_request_status(1, "approved"))
print(get_requests())