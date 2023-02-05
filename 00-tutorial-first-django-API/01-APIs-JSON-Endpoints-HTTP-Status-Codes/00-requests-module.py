import requests


def main():
    #! successful
    # perform get request
    response = requests.get("http://www.google.com")
    # check if request is ok
    print(f"Status code: {response.status_code}\n")
    print(f"Response headers: {response.headers}\n")
    print("Specific response header:", response.headers["Content-Type"], "\n")
    # print(f"Response content: {response.text}") #! prints out a lot of stuff
    print("\n\n")

    #! bad
    response = requests.get("http://www.google.com/some-random-stuff")
    print(f"Status code: {response.status_code}")


if __name__ == "__main__":
    main()
