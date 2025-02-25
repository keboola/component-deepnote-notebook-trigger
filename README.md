Deepnote Notebook Trigger
=============

Deepnote is a collaborative data science notebook.

This component enables you to trigger the running of a specified notebook in Deepnote.

**Table of contents:**

[TOC]

Prerequisites
=============

Get the API token, only available to Team and Enterprise plans of Deepnote.

The generation of the API Key is described in the [api documentation](https://deepnote.com/docs/deepnote-api)

The Notebook and Project ID can be obtained via the URL path to the notebook, described in the [endpoint documentation](https://deepnote.com/docs/api-execute-notebook)

The project ID is a UUID with dashes (e.g. 25fcb3b2-cf3d-4c08-9b24-4306f1518caa) and the notebook ID is a UUID without dashes (e.g. abaf726ac4c34589961a588de29cd665).


Configuration
=============

## Deepnote Trigger configuration

- API Key (#api_token) - [REQ] API key generated in Deepnote
- Project id (project_id) - [REQ] ID of the project in which the notebook is
- Notebook id (notebook_id) - [REQ] The ID of the Notebook to be run

Sample Configuration
=============

```json
{
  "parameters": {
    "#api_token": "SECRET_VALUE",
    "project_id": "25fcb3b2-cf3d-4c08-9b24-4306f1518caa",
    "notebook_id": "abaf726ac4c34589961a588de29cd665"
  }
}
```

Development
-----------

If required, change local data folder (the `CUSTOM_FOLDER` placeholder) path to your custom path in
the `docker-compose.yml` file:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    volumes:
      - ./:/code
      - ./CUSTOM_FOLDER:/data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clone this repository, init the workspace and run the component with following command:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
docker-compose build
docker-compose run --rm dev
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the test suite and lint check using this command:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
docker-compose run --rm test
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Integration
===========

For information about deployment and integration with KBC, please refer to the
[deployment section of developers documentation](https://developers.keboola.com/extend/component/deployment/)