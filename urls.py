from django.conf.urls import patterns, url
urlpatterns = patterns('',
        url(
            r'^password_change$','django.contrib.auth.views.password_change',name='password_change',
            kwargs={
                'template_name':
                'management/pasword_change_form.html',
                'post_change_redirect':'accounts:password_change_done',
                }
            ),
        url(
            r'^password_change_done$',
            'django.contrib.auth.views.password_change_done',
            name='password_change_done',kwargs={'template_name':'management/password_change_done.html'}
            ),
        :
        )
