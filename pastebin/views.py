from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import re


def resolve(request):
	'''
	Yay! A pastebin link resolver
	'''
	if (not request.method == 'GET' or 'url' \
		not in request.GET or 'user' not in request.GET):
		return HttpResponse('invalid request')

	match = re.search('[^\/]+$', request.GET['url'])
	if not match:
		return HttpResponse('url regex mismatch')

	pastebin_code = match.group()

	html_script = (
		'<script src="//pastebin.com/embed_js/' + pastebin_code + '"></script>'
	)

	response = JsonResponse({'body': html_script})

	#Allow CORS
	response['Access-Control-Allow-Origin'] = 'https://compose.mixmax.com'
	response['Access-Control-Allow-Credentials'] = 'true'

	return response
