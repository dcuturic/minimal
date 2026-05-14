# HTML Fragment Wrapper

A minimal solution for wrapping HTML fragments with associated CSS and JavaScript into a cohesive component structure. This tool allows external applications to easily encapsulate UI components by passing raw parts, which are combined into a single portable snippet.

## API Usage
You can interact with this service via the following endpoint:
`POST /api/minimal-solutions/html_fragment_wrapper`

### Request Example
```json
{
  "name": "Card Component",
  "html": "<div class='card'>Hello</div>",
  "css": ".card { color: red; }",
  "js": "console.log('card');"
}
```

### Response Example
```json
{
  "status": "success",
  "data": {
    "wrapped_html": "<!-- Fragment: Card Component -->\n<style>\n.card { color: red; }\n</style>\n<div class='card'>Hello</div>\n<script>\nconsole.log('card');\n</script>"
  }
}
```
