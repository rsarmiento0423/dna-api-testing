"""Base utils for DNA API tests."""
import requests
import os

BASE_URL = "https://dna-api.staging.onec.co/" # "https://api.onecern.com/"  "https://dna-api.staging.onec.co/"
RP_PATH = "v1/location/business-interruption/return-period"
AA_PATH = "v1/location/business-interruption/average-annual"

# DNAAPI_TOKEN = os.environ['DNAAPI_TOKEN']
def call_post_api(url, payload, expect_status_code=200, json=True):
    """call post api"""
    # headers = {"x-1c-api-token": DNAAPI_TOKEN}
    # resp = requests.post(url=url, json=payload, headers=headers, timeout=30)
    resp = requests.post(url=url, json=payload, timeout=60)
    status_code = resp.status_code
    call_post_api.status_code = status_code
    assert status_code == expect_status_code, f"should get status code: {expect_status_code}, but got: {status_code}"

    if json:
        return resp.json()

    return resp
