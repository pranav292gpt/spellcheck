from rest_framework.views import APIView
from rest_framework.response import Response
import re
from utils.corrector import words, correction, extended_corrections, known
from rest_framework import status
from db.models.spell_request import Request

class SpellCorrectorView(APIView):
    def get(self, request, *args, **kwargs):
        if 'text' in request.GET:
            text = request.GET.get('text')
            input_words = words(text)
        
            correct_words = []
            edits = []
            positions = []

            #Getting correct words
            for word in input_words:
                correct_words.append(correction(word))

            def pos(n):
                if n ==0:
                    return 1
                return pos(n-1)+len(input_words[n-1])+1

            #Creating the edits object
            for i, (word, c) in enumerate(zip(input_words, correct_words)):
                if not word==c:
                    edits.append({
                    "id" : i,
                    "word" :word,
                    "correction": c,
                    "extended_corrections": extended_corrections(word),
                    "position" : pos(i)
                        })

            #Joining words after adding space in between
            for word in correct_words:
                correct_text = " ".join(correct_words)

            #Generating the response
            response = {
                    "pre_text" : text,
                    "post_text": correct_text,
                    "edits" : edits
                    }

            #Saving the request object
            request = Request.objects.create(response=response)
            response['request_id'] = request.id

            return Response(response)

        return Response({"error" : "bad request"}, status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        if 'text' in request.POST:
            text = request.POST.get('text')
            input_words = words(text)
 
            correct_words = []
            edits = []
            positions = []

            #Getting correct words
            for word in input_words:
                correct_words.append(correction(word))

            def pos(n):
                if n ==0:
                    return 1
                return pos(n-1)+len(input_words[n-1])+1

            #Creating the edits object
            for i, (word, c) in enumerate(zip(input_words, correct_words)):
                if not word==c:
                    edits.append({
                    "id" : i,
                    "word" :word,
                    "correction": c,
                    "extended_corrections": extended_corrections(word),
                    "position" : pos(i)
                        })

            #Joining words after adding space in between
            for word in correct_words:
                correct_text = " ".join(correct_words)

            #Generating the response
            response = {
                    "pre_text" : text,
                    "post_text": correct_text,
                    "edits" : edits
                    }

            #Saving the request object
            request = Request.objects.create(response=response)
            response['request_id'] = request.id

            return Response(response)

        return Response({"error" : "bad request"}, status.HTTP_400_BAD_REQUEST)
