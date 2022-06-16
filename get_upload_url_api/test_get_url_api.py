"""
Demonstration of how to use the GET Upload details API
"""

import requests
import json
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

if __name__=='__main__':
    file_to_upload = '' # path to the .zip file containing images
    get_upload_details_api_url = 'https://8wvaarvrsc.execute-api.sa-east-1.amazonaws.com/default/fullstack_exam_get_presigned_url'
    get_upload_details_api_token = '' # replace by your token here
    upload_details, batch_id = get_upload_details(get_upload_details_api_url, get_upload_details_api_token)
    upload_response = upload_file_to_s3(file_to_upload, upload_details)
    print(upload_response)