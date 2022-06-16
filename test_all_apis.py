import json
import requests
from typing import Tuple

def get_upload_details(api_url: str, api_token: str) -> Tuple[dict, str]:
    """
    Sends an HTTP GET request and returns the information 
    to upload a file to an s3 bucket and batch id

    Args:
        api_url (str): URL to the get upload details API
        api_token (str): Token to access the API

    Returns:
        upload_details (dict): Information needed to upload the file. 
                               It is valid for 10 minutes.
        batch_id (str): Id of the batch to process. 
                        Should be used later to access the processing status
    """

    header = {'Authorization': f"Bearer {api_token}"}
    response = requests.get(api_url, headers=header)

    if response.status_code!=200:
        print(response)
        exit()

    response_content = json.loads(response.content.decode('utf-8'))
    batch_id = response_content['batch_id']
    upload_details = response_content['upload_details']

    return upload_details, batch_id

def upload_file_to_s3(file_to_upload: str, upload_details: dict) -> requests.models.Response:
    """
    Given the upload information, sends an HTTP POST request to upload the file

    Args:
        file_to_upload (str): Path to the file to upload
        upload_details (dict): Information needed to upload the file

    Returns:
        upload_response (requests.models.Response): Response of the post request
    """

    with open(file_to_upload, 'rb') as f: # opens the zip file as binary
        files = {'file': (file_to_upload, f)}
        upload_response = requests.post(upload_details['url'], data=upload_details['fields'], files=files)
    return upload_response

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

def object_detection(file_to_upload, get_upload_details_api_url, get_upload_details_api_token, get_processing_status_api_url, get_processing_status_api_token):
    
    upload_details, batch_id = get_upload_details(get_upload_details_api_url, get_upload_details_api_token)
    upload_response = upload_file_to_s3(file_to_upload, upload_details)
    processing_status = 'waiting'
    while processing_status not in ['completed', 'failed']:
        status = get_status(batch_id, get_processing_status_api_url, get_processing_status_api_token)
        processing_status = status['processing_status']
        print(status)

    if processing_status=='completed':
        print('[ INFO ] Process Completed.')
    else:
        error_message = status['error_message']
        print(f'[ Error ] Failed to process. Error message: {error_message}')

if __name__=='__main__':
    file_to_upload = '' # path to the zip file
    get_upload_details_api_url = 'https://8wvaarvrsc.execute-api.sa-east-1.amazonaws.com/default/fullstack_exam_get_presigned_url'
    get_upload_details_api_token = '' # replace your token here
    get_processing_status_api_url = 'https://8kad2d3fg6.execute-api.sa-east-1.amazonaws.com/default/full-stack-exam-get-processing-status'
    get_processing_status_api_token = '' # replace your token here

    object_detection(file_to_upload,
                     get_upload_details_api_url,
                     get_upload_details_api_token,
                     get_processing_status_api_url,
                     get_processing_status_api_token)
