import logging

from client import DeepnoteClient, DeepnoteClientException

from keboola.component.base import ComponentBase
from keboola.component.exceptions import UserException

# configuration variables
KEY_API_TOKEN = '#api_token'
KEY_NOTEBOOK_ID = 'notebook_id'
KEY_PROJECT_ID = 'project_id'

# list of mandatory parameters => if some is missing,
# component will fail with readable message on initialization.
REQUIRED_PARAMETERS = [KEY_API_TOKEN, KEY_NOTEBOOK_ID, KEY_PROJECT_ID]
REQUIRED_IMAGE_PARS = []


class Component(ComponentBase):

    def __init__(self):
        super().__init__()

    def run(self):
        self.validate_configuration_parameters(REQUIRED_PARAMETERS)
        self.validate_image_parameters(REQUIRED_IMAGE_PARS)
        params = self.configuration.parameters

        token = params.get(KEY_API_TOKEN)
        notebook_id = params.get(KEY_NOTEBOOK_ID)
        project_id = params.get(KEY_PROJECT_ID)

        client = DeepnoteClient(token)
        logging.info(f"Triggering notebook {notebook_id} in project {project_id}")

        try:
            response = client.start_notebook(project_id, notebook_id)
        except DeepnoteClientException as deepnote_exc:
            raise UserException(deepnote_exc) from deepnote_exc

        logging.info(f"Response from Deepnote : {response.text}")
        logging.info("The notebook has successfully been triggered.")


if __name__ == "__main__":
    try:
        comp = Component()
        # this triggers the run method by default and is controlled by the configuration.action parameter
        comp.execute_action()
    except UserException as exc:
        logging.exception(exc)
        exit(1)
    except Exception as exc:
        logging.exception(exc)
        exit(2)
