from django.http import JsonResponse


def handle_exception(e):
    if len(e.args) == 2:
        return JsonResponse(data=e.args[0], status=e.args[1])
    return JsonResponse(data=e)
