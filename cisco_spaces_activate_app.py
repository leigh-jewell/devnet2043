import jwt
import requests
from datetime import datetime

debug = False


def get_payload(encoded):
    decoded_jwt = jwt.decode(encoded, options={"verify_signature": False}, algorithms=["RS256"])
    keys_returned = decoded_jwt.keys()
    if "appId" not in keys_returned:
        raise Exception("Error: encoded JWT data does not contain appId key.")
    if "activationRefId" not in keys_returned:
        raise Exception("Error: encoded JWT data does not contain activationRefId key.")
    if "expiresIn" not in keys_returned:
        raise Exception("Error: encoded JWT data does not contain expiresIn key")
    try:
        expiration_time = datetime.fromtimestamp(decoded_jwt["expiresIn"]/1000)
    except:
        raise Exception("Error: encoded JWT expiration time invalid.")
    if expiration_time < datetime.now():
        raise Exception(f"Error: the JWT expired on {expiration_time}")
    elif debug:
        print(f"Note: JWT token will expire {expiration_time}")
    return decoded_jwt


def activate(decoded_data, bearer):
    if debug:
        print(f"appId: {decoded_data['appId']} activationRefId:{decoded_data['activationRefId']}")
    headers = {"Authorization": "Bearer " + bearer}
    data = {"appId": decoded_data['appId'],
            "activationRefId": decoded_data['activationRefId']}
    response = requests.post("https://partners.dnaspaces.io/client/v1/partner/activateOnPremiseApp",
                             data=data, headers=headers)
    if response.status_code == 200:
        if debug:
            print("Communication to https://partners.dnaspaces.io succeeded.")
        returned_data = response.json()
        returned_keys = returned_data.keys()
        if "status" in returned_keys:
            if returned_data['status']:
                print(returned_data['message'])
                if "data" in returned_keys:
                    if "apiKey" in returned_data['data']:
                        api_key = returned_data['data']['apiKey']
                        print(f"Got API key.")
                        return api_key
                    else:
                        print("Error: no apiKey provided in data.")
                        return None
                else:
                    print("Error: no data key in returned payload")
                    return None
            else:
                print(f"Error: Activation failed. Status {returned_data['status']} message {returned_data['message']}")
                return None
        else:
            print("Error: no status key returned.")
            return None
    else:
        print(f"Error: Unable to communicate with partners.dnaspaces.io. Got status code {response.status_code}")
        return None


if __name__ == '__main__':
    print("DNA Spaces on-prem app activation.")
    activation_key = input("Activation key:")
    if len(activation_key) > 0:
        decoded = get_payload(activation_key)
        api_key = activate(decoded, activation_key)
        print(f"API Token for activation: {api_key}")