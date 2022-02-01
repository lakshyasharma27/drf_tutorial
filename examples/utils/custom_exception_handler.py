from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first, 
    # to get the standard error response.
    response = exception_handler(exc, context)
    # print(type(exc))
    # print(exc.detail)
    # print(type(exc.detail.__dict__))
    # print(exc.get_codes())
    # print(exc.get_full_details())

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code

    return response

