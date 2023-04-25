from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from gtts import gTTS
import json
from django.views.decorators.csrf import csrf_exempt
from googletrans import Translator, LANGUAGES
import googletrans


def index(request):
    return HttpResponse("Hello, world!")

@csrf_exempt
def tts(request):
    try:
        language = "en"
        data = json.loads(request.body)
        text = data["body"]
        file_name = data["file"]
        speech = gTTS(text=text, lang=language, slow=False)
        speech.save(f"{file_name}.mp3")
        return HttpResponse("TTS conversion successful")
    except Exception as e:
        return HttpResponse(f"TTS conversion failed: {e}")



@csrf_exempt
def translate(request):
    try:
        data = json.loads(request.body)
        text = data['text']

        translator = Translator()
        result = translator.translate(text, src='en', dest='nl')
        translated_text = result.text

        return HttpResponse(translated_text)
    except Exception as e:
        return HttpResponse(f"conversion failed: {e}")


def get_languages(request):
    """
    Returns a JSON response with all the available languages for translation
    """
    source_languages = googletrans.LANGUAGES
    destination_languages = googletrans.LANGUAGES
    return JsonResponse({
        "source_languages": source_languages,
        "destination_languages": destination_languages
    })

