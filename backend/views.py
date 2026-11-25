from model import Request
from form import RequestForm

requests = []


def create_request(data):
    form = RequestForm(data)

    if not form.is_valid():
        return {
            "success": False,
            "errors": form.errors
        }

    request_id = len(requests) + 1

    new_request = Request(
        request_id=request_id,
        title=data["title"],
        description=data["description"]
    )

    requests.append(new_request)

    return {
        "success": True,
        "message": "Request created successfully",
        "data": new_request.get_details()
    }


def get_requests():
    return {
        "success": True,
        "data": [request.get_details() for request in requests]
    }


def update_request_status(request_id, new_status):
    for request in requests:
        if request.request_id == request_id:
            request.update_status(new_status)

            return {
                "success": True,
                "message": "Request status updated successfully"
            }

    return {
        "success": False,
        "message": "Request not found still"
    }