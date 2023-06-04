from flask import Flask, jsonify, request
from dotenv import load_dotenv
import requests
import os

load_dotenv()

token = os.getenv('AUTH_TOKEN')

app = Flask(__name__)

@app.route('/listNftByOwnerAndContract', methods=['POST'])
def listNftByOwnerAndContract():
    url = "https://web3.luniverse.io/v1/polygon/mumbai/nft/listNftByOwnerAndContract"
    payload = request.get_json()

    contract_address = payload.get('contractAddress')
    owner_address = payload.get('ownerAddress')

    payload = {"contractAddress": contract_address, "ownerAddress": owner_address}
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.text

@app.route('/listNftContractMetadataByContract', methods=['POST'])
def listNftContractMetadataByContract():
    url = "https://web3.luniverse.io/v1/polygon/mumbai/nft/listNftContractMetadataByContract"
    payload = request.get_json()

    contract_address = payload.get('contractAddress')

    payload = {"contractAddresses": [contract_address]}
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.text

@app.route('/listNftContractMetadataByOwner', methods=['POST'])
def listNftContractMetadataByOwner():
    url = "https://web3.luniverse.io/v1/polygon/mumbai/nft/listNftContractMetadataByOwner"
    payload = request.get_json()

    owner_address = payload.get('ownerAddress')

    payload = {"ownerAddress": owner_address}
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.text

@app.route('/getNftMetadataByTokenId', methods=['POST'])
def getNftMetadataByTokenId():
    url = "https://web3.luniverse.io/v1/polygon/mumbai/nft/getNftMetadataByTokenId"
    payload = request.get_json()

    contract_address = payload.get('contractAddress')
    token_id = payload.get('tokenId')

    payload = {"contractAddress": contract_address, "tokenId": token_id}
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.text

if __name__ == '__main__':
    app.run()
