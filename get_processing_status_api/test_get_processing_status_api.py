import requests
import json

def get_status(batch_id: str, get_processing_status_api_url: str, get_processing_status_api_token: str) -> dict:
    """
    Sends an HTTP GET request to get the processing status of the batch id

    Args:
        batch_id (str): batch id to get the status
        get_processing_status_api_url (str): URL to the get processing status API
        get_processing_status_api_token (str): Token to access the API

    Returns:
        dict: dictionary containing the status of the batch id
    """
    header = {'Authorization': f"Bearer {get_processing_status_api_token}"}
    response = requests.get(f'{get_processing_status_api_url}?batch_id={batch_id}', headers=header)
    status = response.content.decode('utf-8')
    status = json.loads(status)
    return status

if __name__=='__main__':
    batch_id = '' # replace by the batch id here
    get_processing_status_api_url = 'https://8kad2d3fg6.execute-api.sa-east-1.amazonaws.com/default/full-stack-exam-get-processing-status'
    get_processing_status_api_token = '' # replace by your token here
    status = get_status(batch_id, get_processing_status_api_url, get_processing_status_api_token)
    print(status)