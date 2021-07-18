import requests
import json
import qrcode
from web3.auto import w3
from eth_account.messages import encode_defunct

def getRawMessage():
    # Function to get message to sign from axie

    # An exemple of a requestBody needed
    requestBody = {"operationName":"CreateRandomMessage","variables":{},"query":"mutation CreateRandomMessage {\n  createRandomMessage\n}\n"}
    # Send the request
    r = requests.post('https://axieinfinity.com/graphql-server-v2/graphql', headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',}, data=requestBody)
    # Load the data into json format
    json_data = json.loads(r.text)
    # Return the message to sign
    return json_data['data']['createRandomMessage']

def getSignMessage(rawMessage, accountPrivateKey):
    # Function to sign the message got from getRawMessage function

    # Load the private key from the DataBase in Hex
    private_key = bytearray.fromhex(accountPrivateKey)
    message = encode_defunct(text=rawMessage)
    # Sign the message with the private key
    hexSignature = w3.eth.account.sign_message(message, private_key=private_key)
    # Return the signature
    return hexSignature

def submitSignature(signedMessage, message, accountAddress):
    # Function to submit the signature and get authorization

    # An example of a requestBody needed
    requestBody = {"operationName":"CreateAccessTokenWithSignature","variables":{"input":{"mainnet":"ronin","owner":"User's Eth Wallet Address","message":"User's Raw Message","signature":"User's Signed Message"}},"query":"mutation CreateAccessTokenWithSignature($input: SignatureInput!) {\n  createAccessTokenWithSignature(input: $input) {\n    newAccount\n    result\n    accessToken\n    __typename\n  }\n}\n"}
    # Remplace in that example to the actual signed message
    requestBody['variables']['input']['signature'] = signedMessage['signature'].hex()
    # Remplace in that example to the actual raw message
    requestBody['variables']['input']['message'] = message
    # Remplace in that example to the actual account address
    requestBody['variables']['input']['owner'] = accountAddress
    # Send the request
    r = requests.post('https://axieinfinity.com/graphql-server-v2/graphql', headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',}, json=requestBody)
    # Load the data into json format
    json_data = json.loads(r.text)
    # Return the accessToken value
    return json_data['data']['createAccessTokenWithSignature']['accessToken']
    return
