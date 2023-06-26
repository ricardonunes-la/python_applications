from googlesearch import search

def search_google(query, num_results):
    search_results = []

    # Perform a Google search
    for result in search(query, lang='en', stop=num_results, pause=2):
        search_results.append(result)

    # Display the results
    for i, result in enumerate(search_results, start=1):
        print(f"Result {i}: {result}")

# Example of use
search_query = "telomeres"
num_results = 10

search_google(search_query, num_results)
