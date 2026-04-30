# tta-web

## Deploying with Coolify

Use the included `Dockerfile`.

Coolify settings:
- Build Pack: `Dockerfile`
- Port: `8000`

Required environment variables:

```env
DEBUG=false
SECRET_KEY=replace-with-a-long-random-secret
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
CSRF_TRUSTED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
```

Email delivery environment variables:

```env
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.your-provider.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-smtp-user
EMAIL_HOST_PASSWORD=your-smtp-password
EMAIL_USE_TLS=true
DEFAULT_FROM_EMAIL=TRANSTRADE AFRICA Website <no-reply@yourdomain.com>
```

The contact form sends inquiries to `info@transtradeafrica.rw`.
