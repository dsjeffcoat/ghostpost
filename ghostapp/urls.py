from django.urls import path
from ghostapp import views as v

urlpatterns = [
    path('', v.index, name="homepage"),
    path('votes/', v.votes_view, name="votes"),
    path('upvote/<int:post_id>/', v.upvote_view, name="upvote"),
    path('downvote/<int:post_id>/', v.downvote_view, name="downvote"),
    path('boasts/', v.boasts_view, name="boasts"),
    path('roasts/', v.roasts_view, name="roasts"),
    path('add-post/', v.createpost_view, name="createpost"),
    path('detail/<str:sec_key>', v.detail_view, name="postdetail"),
    path('delete/<int:post_id>/', v.deletepost_view, name="deletepost"),
]
