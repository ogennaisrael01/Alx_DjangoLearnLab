This document provides a comprehensive overview of Django's built-in security features. It explains what each feature does, why it's important, and how to configure it correctly for a production environment.

1. DEBUG = False
Purpose: Disables detailed error pages.
Why: When DEBUG is True, stack traces, environment variables, and database information may be exposed in error pages—posing a major security risk.
How:

python
Copy
Edit
DEBUG = False
2. ALLOWED_HOSTS
Purpose: Prevents HTTP Host header attacks.
Why: Django will only allow requests from hosts explicitly listed.
How:

python
Copy
Edit
ALLOWED_HOSTS = ['yourdomain.com', 'localhost']
3. HTTPS & SSL Settings
Purpose: Ensures all data is encrypted in transit.
Why: Protects sensitive data like login credentials and session cookies.
How:

python
Copy
Edit
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
4. HTTP Security Headers
a. SECURE_BROWSER_XSS_FILTER
Purpose: Enables browser’s XSS protection.
How:

python
Copy
Edit
SECURE_BROWSER_XSS_FILTER = True
b. SECURE_CONTENT_TYPE_NOSNIFF
Purpose: Prevents MIME-type sniffing.
How:

python
Copy
Edit
SECURE_CONTENT_TYPE_NOSNIFF = True
c. X_FRAME_OPTIONS
Purpose: Prevents clickjacking.
How:

python
Copy
Edit
X_FRAME_OPTIONS = 'DENY'
d. SECURE_REFERRER_POLICY
Purpose: Restricts referrer information sent by the browser.
How:

python
Copy
Edit
SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'
5. Content Security Policy (CSP)
Purpose: Limits the sources from which content (scripts, styles, etc.) can be loaded.
Why: Mitigates many forms of Cross-Site Scripting (XSS) attacks.
How:

Install the CSP package:

bash
Copy
Edit
pip install django-csp
Update settings.py:

python
Copy
Edit
INSTALLED_APPS += ['csp']
MIDDLEWARE += ['csp.middleware.CSPMiddleware']
CSP_DEFAULT_SRC = ("'self'",)