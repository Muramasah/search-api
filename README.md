<h1 align="center">Web Expeditious Retrieval - Search API</h1>

WER Search API is a python backend service which provides the means to perform text-based search over the unified navigation history

## Project building philosophy

The project was developed focused on delivery a ___proof of concept___, because of that, there are no tests and it code is softly typed. The philosophy behind this decision is that typing and test code that relies on little used libraries and discover how to implement a solution that it was never approached, will slow down the development by adding unknowns and extending the code base that will work with those unknowns.

The next first step to build a scalable solution will be adding tests.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the.

```bash
pip install -r requirements.txt
```

## Usage

The backend service listens for connections at `http://localhost:8888`. To execute the it run:

```bash
python ./src/server/wer.py
```

## API

The API handles only one resource, **website**.

### PUT /search_api/v1/websites

```
| Parameter | Type     | Description                                             |
| :-------- | :------- | :------------------------------------------------------ |
| `text`    | `string` | **Required**. The text content of a website.            |
| `url`     | `string` | **Required**. The website url, it will work as uniq ID. |
| `title`   | `string` | **Required**. The website title                         |
```

#### Usage

This endpoint will index a website or it will update an existing one if the url is already present.

```http
PUT /search_api/v1/websites
```

#### Response

After a successful call, the response will contain a 201 http status code and a message:

| Status Code | Description                                               |
| :---------- | :-------------------------------------------------------- |
| 201         | `Text content from {website.title} indexed successfully'` |

### GET /search_api/v1/websites

```
| Parameter | Type     | Description                                               |
| :-------- | :------- | :-------------------------------------------------------- |
| `query`   | `string` | **Required**. Your query to search over the website texts |
```

#### Usage

Use words separated with spaces to searching for words in the search index:

```http
GET /search_api/v1/websites?query=there%20are
```

Use quotes to searching to exact phrase in the search index:

```http
GET /search_api/v1/websites?query="there%20are"
```

#### Response

After a successful call, the results will be provided in an array of results

```javascript
[
  {
    title: string,
    url: string,
  },
];
```

## License

[MIT](LICENSE)
