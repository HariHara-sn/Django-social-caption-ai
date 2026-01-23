from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import GeneratePostSerializer
from .services.content_service import generate_post_content

class GeneratePostAPIView(APIView):
    def post(self, request):
        serializer = GeneratePostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        content = generate_post_content(
            serializer.validated_data["platform"],
            serializer.validated_data["contextTerm"]
        )

        return Response(
            {
                "platform": serializer.validated_data["platform"],
                "contextTerm": serializer.validated_data["contextTerm"],
                "content": content
            },
            status=status.HTTP_200_OK
        )
