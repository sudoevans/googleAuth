# GoogleAuth


!["snave_pic"](https://github.com/gamer-snave/googleAuth/blob/main/static/img/download.png)
!["snave_pic"](https://github.com/gamer-snave/googleAuth/blob/main/static/img/snave.png)
!['another"](https://github.com/gamer-snave/googleAuth/blob/main/static/img/google.png)

---
## Google User Authentication using Django
To add Google login on your app, you’ll need to set up OAuth application via [Google Console](https://console.cloud.google.com/apis/dashboard)

    # Add the following to installed Apps under project_name/settings.
``` 'django.contrib.sites', 
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google', # for Google OAuth 2.0'
    ]
```
## backend and configuration settings
```AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
]
```
## Continue to add SITE_ID and specify redirect URL upon successful Google login. You can also add additional configuration settings as shown below:
```SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
```
*b e Keen with the SITE_ID,* 

## Additional configuration settings
``` SOCIALACCOUNT_QUERY_EMAIL = True
ACCOUNT_LOGOUT_ON_GET= True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True
Finally, enable email scope to receive user’s email addresses after successful social login:
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
  ```
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}
## urls.py
Go to urls.py file of your project directory and add the allauth urls and specify include on top of import.

We add a route /accounts that includes all django-allauth URLs. All OAuth operations will be performed under this route.

```from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
```

### Happy pulling felas!

