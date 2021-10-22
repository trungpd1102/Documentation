swagger: '2.0'
info:
  version: 0.0.0
  title: Markdown 
  description: |
    # Heading

    Text attributes _italic_, *italic*, __bold__, **bold**, `monospace`.

    Horizontal rule:

    ---

    Bullet list:

      * apples
      * oranges
      * pears

    Numbered list:

      1. apples
      2. oranges
      3. pears

    A [link](http://example.com).

    An image:
    ![Swagger logo](https://raw.githubusercontent.com/swagger-api/swagger-ui/master/dist/favicon-32x32.png)

    Code block:

    ```
    {
      "message": "Hello, world!"
    }
    ```

    Tables:

    | Column1 | Column2 |
    | ------- | --------|
    | cell1   | cell2   |
paths:
  /:
    get:
      responses:
        200:
          description: OK
