from django.http import HttpResponse
from ref_api.models import Chromosome

SUPPORTED_ENCODINGS = ['text/plain']
CIRCULAR_CHROMOSOME_SUPPORT = True


def get_sequence_by_id(request, trunc512_id):
    if not Chromosome.objects.filter(trunc512=trunc512_id).exists():
        return HttpResponse('ID does not exist', status=404)

    chromosome = Chromosome.objects.get(trunc512=trunc512_id)

    if request.META['HTTP_ACCEPT'] not in SUPPORTED_ENCODINGS:
        return HttpResponse('Encoding not supported by the server', status=415)

    if 'HTTP_RANGE' not in request.META and request.GET == {}:
        return HttpResponse(
            chromosome.sequence,
            content_type='text/vnd.ga4gh.seq.v1.0.0+plain; charset=us-ascii',
            status=200)

    if 'HTTP_RANGE' in request.META and request.GET != {}:
        return HttpResponse(
            'Both Range and query params are givern',
            status=400)

    if 'start' and 'end' in request.GET:
        start = request.GET['start']
        end = request.GET['end']
        if not start.isdigit() or not end.isdigit():
            return HttpResponse(
                'start and end query parameters support only integer type',
                status=400)
        start = int(start)
        end = int(end)
        if start >= chromosome.size or end > chromosome.size:
            return HttpResponse(
                'start and end query parameters are out of bounds',
                status=400)
        if start > end:
            if CIRCULAR_CHROMOSOME_SUPPORT is False:
                return HttpResponse(
                    'Circular chromosome not implemented yet',
                    status=501)
            else:
                if chromosome.is_circular == 0:
                    return HttpResponse(
                        'Range not satisfiable',
                        status=416)
                else:
                    return HttpResponse(
                        chromosome.sequence[start:chromosome.size] + chromosome.sequence[0:end],
                        content_type='text/vnd.ga4gh.seq.v1.0.0+plain; charset=us-ascii',
                        status=200)
        if start < end:
            return HttpResponse(
                chromosome.sequence[start:end],
                content_type='text/vnd.ga4gh.seq.v1.0.0+plain; charset=us-ascii',
                status=200)

    if 'HTTP_RANGE' in request.META:
        range_head = request.META['HTTP_RANGE']
        if range_head[0:5] != 'bytes':
            return HttpResponse(
                'Invalid unit in Range, use bytes',
                status=400)
        else:
            if range_head[5] != '=':
                return HttpResponse(
                    'Invalid format in Range',
                    status=400)
            else:
                x, y = range_head[6:].split('-')
                x = int(x)
                y = int(y)
                if x >= chromosome.size or y >= chromosome.size:
                    return HttpResponse(
                        'Range out of bounds',
                        status=400)
                if x > y:
                    return HttpResponse(
                        'Can not process circular chromosomes using Range',
                        status=400)
                return HttpResponse(
                    chromosome.sequence[x:y+1],
                    content_type='text/vnd.ga4gh.seq.v1.0.0+plain; charset=us-ascii',
                    status=206)

    return HttpResponse(
        'Kindly review your request. Something went wrong',
        status=400)
