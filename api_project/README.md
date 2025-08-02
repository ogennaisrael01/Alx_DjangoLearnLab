## 🔐 Authentication

This API uses **Token Authentication** as the primary method, with **Basic Authentication** as a fallback.

### ✅ 1. Token Authentication (Primary)

- Clients must obtain a token by sending a `POST` request to `/api/token/`
- Once you receive a token, include it in all requests:

Authorization: Token <your_token_here>

pgsql
Copy
Edit

**Example (Postman):**

- Method: `POST`
- URL: `http://127.0.0.1:8000/api/token/`
- Body (JSON):
```json
{
  "username": "admin",
  "password": "adminpass"
}
Response:

json
Copy
Edit
{ "token": "abc123tokenvalue" }
Use the returned token in the Authorization header for all protected endpoints.