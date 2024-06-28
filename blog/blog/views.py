from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'message': 'Welcome to the API!',
        'info': 'This is a simple API endpoint.'
    })

@api_view(['GET'])
def api_posts(request, format=None):
    posts = [
        {'id': 1, 'title': 'Post 1', 'content': 'Content of post 1'},
        {'id': 2, 'title': 'Post 2', 'content': 'Content of post 2'},
    ]
    return Response(posts)

@api_view(['GET'])
def api_post_by_id(request, id, format=None):
    post = {'id': id, 'title': f'Post {id}', 'content': f'Content of post {id}'}
    return Response(post)
