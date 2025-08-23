# Accounts App

This app handles user authentication and profile management for the Social Media API project.

## Features

- Custom user model (`CustomUser`) with email as the unique identifier
- User registration and login via API endpoints
- Token-based authentication
- User profile fields: bio, profile picture, followers/following
- Serializers for registration and login
- Custom authentication backend for email login

## API Endpoints

- `POST /api/accounts/register/` — Register a new user
- `POST /api/accounts/login/` — Login and receive an authentication token

## Models

- `CustomUser`: Extends Django's `AbstractUser` and `PermissionsMixin`
  - Fields: email, bio, followers, profile_picture

## Usage

1. Add `'accounts'` to your `INSTALLED_APPS` in `settings.py`.
2. Run migrations to create the custom user table.
3. Use the provided API endpoints for registration and login.

## Tests

Basic tests for registration and login are included in `accounts/tests.py`.

---

### Commit Message
