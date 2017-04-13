from rest_framework.views import APIView
from rest_framework.response import Response
import re
from utils.corrector import words, correction

class SpellCorrectorView(APIView):

    def get(self, request, *args, **kwargs):
        text = request.GET['text']
        input_words = words(text)
        print input_words 
        
        correct_words = []
        for word in input_words:
            correct_words.append(correction(word))

        for word in correct_words:
            correct_text = " ".join(correct_words)
        print correct_words 
        return Response({"Correct Text" : correct_text})
    
