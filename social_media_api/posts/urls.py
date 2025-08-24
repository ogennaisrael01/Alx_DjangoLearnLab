from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts.views import PostApiView, CommentCreateApiView, CommentListApiView, CommentDetailApiView

routers = DefaultRouter()
routers.register(r'post', PostApiView)
# routers.register(r'comment', CommentDetailApiView)
urlpatterns = [
    path('', include(routers.urls)),
    path('post/<int:pk>/comment/', CommentCreateApiView.as_view(), name="comment"),
    path("post/<int:pk>/comment/list/", CommentListApiView.as_view(), name="list_comment"),
    path("post/<int:pk>/comment/<int:comment_id>/", CommentDetailApiView.as_view(), name="comment_detail")
]