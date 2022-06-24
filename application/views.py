import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import BlogMetadata
from .serializers import BlogMetadataSerializer


def insert_blogs_to_db(blogs):
    bulk_data = [BlogMetadata(user_id=blog.get("userId"), title=blog.get("title"), body=blog.get("body")) for blog in blogs]
    BlogMetadata.objects.bulk_create(bulk_data)


@api_view(["POST"])
def parse_file_data(request):
    file_ref = request.data.get("file")
    try:
        blogs = json.load(file_ref)
        insert_blogs_to_db(blogs)
    except Exception as e:
        print(e)
        return Response({"message": "Unable to parse file"}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"message": "All data stored to DB"}, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_all_data(request):
    data = BlogMetadata.objects.all()
    serializer = BlogMetadataSerializer(data, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def initial_handshake(request):
    username = request.user.username
    return Response({"name": username})
