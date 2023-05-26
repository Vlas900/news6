from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, SearchList, ArticleCreateView, \
   ArticleUpdateView, ArticleDeleteView, BaseRegisterView, IndexView, upgrade_me, CategoryListView, subscribe
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
   path('news/', PostList.as_view(), name='post_list'),
   path('news/<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('news/create/',  PostCreate.as_view(), name='create_post'),
   path('news/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('news/search/', SearchList.as_view(), name='news_search'),
   path('articles/create/', ArticleCreateView.as_view(), name='create_article'),
   path('articles/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_update'),
   path('articles/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
   path('login/', LoginView.as_view(template_name='login.html'), name='login'),
   path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
   path('signup/', BaseRegisterView.as_view(template_name='signup.html'), name='signup'),
   path('sing/', IndexView.as_view()),
   path('upgrade/', upgrade_me, name='upgrade'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe')
]