from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
# from django.core.files.uploadedfile import UploadedFile
from django.views.decorators.csrf import csrf_exempt

from models import DropzoneImage

import json


def dropzone(request):
    return render(request, "dropzone_test/index.html", {})


@csrf_exempt
def dropzone_upload(request):
    return HttpResponse(json.dumps({'success': True}))


@csrf_exempt
def delete(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        dz_image = get_object_or_404(DropzoneImage, key=key)
        dz_image.delete()

        return HttpResponse(json.dumps({'success': True}))
    else:
        return HttpResponse(json.dumps({'success': False, 'error': 'Only POST allowed.'}))


@csrf_exempt
def upload(request):
    results = {}
    if request.method == 'POST':
        if request.FILES is None:
            return HttpResponseBadRequest('No files attached.')
        f = request.FILES['file']

        dz_image = DropzoneImage()

        # Generate the key to be used as thefilename.
        # Imgur-esque, but only use six characters
        dz_image.key = dz_image.generate_key()

        # f.name.split(".")[-1] grabs the extension of the file name.
        f.name = '%s.%s' % (dz_image.key, f.name.split(".")[-1])

        dz_image.image = f
        dz_image.save()

        results['success'] = True
        results['key'] = dz_image.key
        results['filename'] = f.name
    else:
        results['success'] = False

    return HttpResponse(json.dumps(results), mimetype='application/json')
