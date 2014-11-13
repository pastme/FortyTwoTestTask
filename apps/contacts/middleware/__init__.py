from apps.contacts.models import RequestData


class RequestToDbMiddleware(object):

    def process_request(self, request):
        request_data = RequestData(data=str(request))
        request_data.save()

