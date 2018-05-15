from django.http import HttpResponse
from ref_api.models import Chromosome

SUPPORTED_ENCODINGS = ['text/plain']


def get_sequence_by_id(request, trunc512_id):
    if not Chromosome.objects.filter(trunc512=trunc512_id).exists():
        return HttpResponse('ID does not exist', status=404)

    if request.META['HTTP_ACCEPT'] not in SUPPORTED_ENCODINGS:
        return HttpResponse('Encoding not supported by the server', status=415)

    if 'HTTP_RANGE' not in request.META and request.GET == {}:
        return HttpResponse(
            Chromosome.objects.get(trunc512=trunc512_id).sequence,
            content_type=' text/vnd.ga4gh.seq.v1.0.0+plain',
            status=200)

    if 'HTTP_RANGE' in request.META and request.GET != {}:
        return HttpResponse(
            'Both Range and query params are givern',
            status=400)
