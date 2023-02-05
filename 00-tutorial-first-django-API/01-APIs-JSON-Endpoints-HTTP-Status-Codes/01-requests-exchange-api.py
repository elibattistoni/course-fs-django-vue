# https://exchangerate.host/#/

import requests


def example_request_1():
    #! NB the URL is the endpoint to which you sent the request
    response = requests.get("https://api.exchangerate.host/latest")
    print(f"Status code: {response.status_code}\n")

    #! raise error if failed request
    if response.status_code != 200:
        print(f"Error! Response: {response}")
        raise Exception("There was an error!")

    #! the content type is application/json
    print("Specific response header:", response.headers["Content-Type"], "\n")

    data = response.json()
    print("JSON data: ", data)
    print("---------------------------------------------------")


def example_request_2():
    #! cool way of defining params of an endpoint!
    #! full endpoint: 'https://api.exchangerate.host/convert?from=USD&to=EUR'
    payload = {"from": "USD", "to": "EUR"}
    #! in this way the parameters are automatically added to our endpoint
    response = requests.get("https://api.exchangerate.host/convert", params=payload)
    print(f"Status code: {response.status_code}\n")

    if response.status_code != 200:
        print(f"Error! Response: {response}")
        raise Exception("There was an error!")

    print("Specific response header:", response.headers["Content-Type"], "\n")

    data = response.json()
    print("JSON data: ", data)
    print("---------------------------------------------------")


def main():
    example_request_1()
    example_request_2()


if __name__ == "__main__":
    main()
