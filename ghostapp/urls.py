from django.urls import path
from ghostapp.views import index, votes_view, upvote_view, downvote_view, boasts_view, roasts_view, createpost_view

urlpatterns = [
    path('', index, name="homepage"),
    path('votes/', votes_view, name="votes"),
    path('upvote/<int:post_id>/', upvote_view, name="upvote"),
    path('downvote/<int:post_id>/', downvote_view, name="downvote"),
    path('boasts/', boasts_view, name="boasts"),
    path('roasts/', roasts_view, name="roasts"),
    path('add-post/', createpost_view, name="createpost"),
]
