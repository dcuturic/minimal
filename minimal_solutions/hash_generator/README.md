# Hash Generator

A minimal solution for generating cryptographic hashes from text input.

## Usage

### UI
The User Interface can be accessed at:
`/minimal-solutions/hash_generator`

### API Integration

The Hash Generator functionality can also be integrated into external systems via our API.

**Endpoint:** `POST /api/minimal-solutions/hash_generator`

**Request Example:**
```json
{
  "text": "secret password",
  "algorithm": "sha256"
}
```

**Response Example:**
```json
{
  "status": "success",
  "data": {
    "result": "2b6b66b69b50b73c4d7e29cf47fc8f2445cf0241db86f56c0b31dff7e4eb1202",
    "algorithm": "sha256"
  }
}
```

The supported algorithms are `md5`, `sha1`, `sha256`, and `sha512`.
