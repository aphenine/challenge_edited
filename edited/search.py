
import argparse
import json
from math import ceil
from pathlib import Path


def load_data(location: Path) -> list:
    with open(location) as data_source:
        data = json.loads(data_source.read())

    return data


class Result:
    def __init__(self, data, score):
        self.data = data    # Pointer to data
        self.score = score  # Score value

    def __str__(self):
        return f"({self.score}: {self.data})"

    def __repr__(self):
        return self.__str__()


def search(data, search_term):
    """A function that does our search on a set of data and returns results"""
    # Super simple search function to help test things first
    results = []
    for item in data:
        score = 0
        terms = search_term.split(" ")

        # Just check whether the terms occur in the text
        for term in terms:
            if term in item["brand"]:
                score += 5
            if term in item["name"]:
                score += 5

        if score > 0:
            results.append(Result(item, score))

    return results


def batch_search(search_term, data, search_func, chunk_size=10000):
    """A function that stages our data on the search function and batch prossesses the results"""
    # The number of chunks we're going to split the data search in
    num_chunks = ceil(len(data) / chunk_size)
    results = []
    for i in range(0, num_chunks):
        last_chunk = i == num_chunks - 1    # Extra var for readability
        if last_chunk:
            data_chunk = data[i*chunk_size:]
        else:
            data_chunk = data[i*chunk_size: (i+1) * chunk_size]

        batch_results = search_func(data_chunk, search_term)
        results.extend(batch_results)

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Edited Search Tool")
    parser.add_argument(
        "search",
        nargs="+",
        help="The search terms you would look to look for"
    )
    parser.add_argument(
        "--data", "-d",
        dest="data",
        default="./search_dataset.json"
    )

    args = parser.parse_args()
    print(args)
    
    data = load_data(Path(args.data))

    # print(data)

    # Relink up search term (we might want to reprocess it)
    search_term = " ".join(args.search)

    # Batch process the search
    results = batch_search(search_term, data, search, 10000)

    # Sort the actual results
    results.sort(key=lambda x: x.score)

    print(results)
