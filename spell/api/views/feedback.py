from rest_framework.views import APIView
from db.models.spell_request import Request
from rest_framework.response import Response
from rest_framework import status

class FeedbackView(APIView):
    def get(self, request, *args, **kwargs):
        if 'request_id' and 'feedback' in request.GET:

            request_id = request.GET.get("request_id")
            feedback = request.GET.get("feedback")

            try:
                request = Request.objects.get(id=request_id)
                request.feedback=feedback
                request.save(update_fields=['feedback'])

                return Response({
                "status": 200,
                "comment": "Feedback accepted. Thanks!"
                        })
            except Exception:
                return Response({"error" : "request object not found"}, status.HTTP_404_NOT_FOUND)
        return Response({"error" : "bad request"}, status.HTTP_400_BAD_REQUEST)
