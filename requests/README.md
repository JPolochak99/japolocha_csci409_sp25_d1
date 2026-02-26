# CatFact API Script

## API Chosen
I used the CatFact API (https://catfact.ninja/) because it is free and simple to get data about cats, like facts and breeds.

## What the script does
- Makes three requests to the API:
  1. Get a list of cat breeds.
  2. Get a random cat fact.
  3. Get a random short cat fact with a max length of 50 characters.
- Prints some of the data in a readable format.
- Saves all responses to JSON files for future analysis.
- Includes basic error handling for timeouts or failed requests.
- Uses a custom header (`User-Agent`) and query parameter (`max_length`).

## Challenges faced
- Figuring out how to loop through the JSON data from `/breeds`.
- Understanding how to use query parameters.
- understanding all aspects of the script.
- figuring out how json files are structured
 
## Example output
**breeds.json**
```json
{
    "current_page": 1,
    "data": [
        {
            "breed": "Abyssinian",
            "origin": "Ethiopia",
            "country": "EG",
            "coat": "short",
            "pattern": "ticked"
        },
        {
            "breed": "Aegean",
            "origin": "Greece",
            "country": "GR",
            "coat": "short",
            "pattern": "ticked"
        }
    ]
}
