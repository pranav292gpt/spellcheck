from rest_framework.views import APIView
from rest_framework.response import Response
import re
from utils.corrector import words, correction, extended_corrections, known
from rest_framework import status

class SpellCorrectorView(APIView):

    def get(self, request, *args, **kwargs):
        if 'text' in request.GET:
            text = request.GET.get('text')
            input_words = words(text)
        
            correct_words = []
            edits = []
            positions = []

            for word in input_words:
                correct_words.append(correction(word))

            def pos(n):
                if n ==0:
                    return 1
                return pos(n-1)+len(input_words[n-1])+1
    
            for i, (word, c) in enumerate(zip(input_words, correct_words)):
                if not word==c:
                    edits.append({
                    "id" : i,
                    "word" :word,
                    "correction": c,
                    "extended_corrections": extended_corrections(word),
                    "position" : pos(i)
                        })

            for word in correct_words:
                correct_text = " ".join(correct_words)

            response = {
                    "pre_text" : text,
                    "post_text": correct_text,
                    "edits" : edits
                    }

            return Response(response)

        return Response({"error" : "bad request"}, status.HTTP_400_BAD_REQUEST)
