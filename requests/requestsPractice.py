import requests
import json

BASE_URL = "https://catfact.ninja/"

#GET: List of breeds
try:
    response = requests.get(f"{BASE_URL}/breeds",  timeout=5)
    response.raise_for_status()
    data = response.json()

    print("Breeds request success!")
    for breed in data["data"][:5]:  # this for loop will only print the fist 5 breeds
        print(f"Breed: {breed['breed']}, Origin: {breed['origin']}")

    # save to file
    with open("breeds.json", "w") as f:
        json.dump(data, f, indent=4)

except requests.exceptions.Timeout:
    print("Breeds request timed out!")
except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)
except requests.exceptions.RequestException as e:
    print("Something went wrong with the request:", e)


# GET: Random cat fact
try:
    response = requests.get(f"{BASE_URL}/fact", timeout=5)
    response.raise_for_status()
    fact_data = response.json()

    print("\nRandom fact request success!")
    print("Random fact:", fact_data["fact"])

    with open("random_fact.json", "w") as f:
        json.dump(fact_data, f, indent=4)

except requests.exceptions.RequestException as e:
    print("❌ Random fact request failed:", e)


# GET: Fact with query parameter (length)
params = {"max_length": 50}  # parameter
try:
    response = requests.get(f"{BASE_URL}/fact", params=params, timeout=5)
    response.raise_for_status()
    short_fact_data = response.json()

    print("\nShort fact request success!")
    print("Short fact:", short_fact_data["fact"])

    with open("short_fact.json", "w") as f:
        json.dump(short_fact_data, f, indent=4)

except requests.exceptions.RequestException as e:
    print("Short fact request failed:", e)