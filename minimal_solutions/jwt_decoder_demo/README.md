# JWT Decoder Demo

Diese Minimal-Lösung bietet eine einfache Möglichkeit, JSON Web Tokens (JWT) zu decodieren und deren Header sowie Payload auszulesen.

## Verwendung der Schnittstelle (Extern)

Die Schnittstelle kann problemlos von externen Applikationen, Services oder Skripten genutzt werden, um JSON Web Tokens automatisiert zu decodieren. Sende dazu einfach einen `POST`-Request mit dem zu decodierenden Token als JSON im Request-Body an den untenstehenden Endpunkt.

### Endpoint

`POST /api/minimal-solutions/jwt_decoder_demo`

### Request-Beispiel

```json
{
  "jwt": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
}
```

### Response-Beispiel (Erfolg)

```json
{
  "status": "success",
  "data": {
    "header": {
      "alg": "HS256",
      "typ": "JWT"
    },
    "payload": {
      "sub": "1234567890",
      "name": "John Doe",
      "iat": 1516239022
    }
  }
}
```

### Response-Beispiel (Fehler)

```json
{
  "status": "error",
  "message": "Ungültiges JWT Format."
}
```
