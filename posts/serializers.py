from rest_framework import serializers

class GeneratePostSerializer(serializers.Serializer):
    platform = serializers.ChoiceField(
        choices=["instagram", "linkedin", "twitter", "facebook", "youtube"]
    )
    contextTerm = serializers.CharField(max_length=100)
