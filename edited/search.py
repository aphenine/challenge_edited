
import argparse
import json
from math import ceil
from pathlib import Path

import spacy

nlp = spacy.load("en_core_web_sm")


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


def super_simple_search(data, search_term):
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


def nlp_search(data, search_term):
    """Use natural language processing to grab the search terms"""
    # Find named entities, phrases and concepts
    doc = nlp(search_term)

    results = []
    for item in data:
        # If we can check out an entity that we know, look for it in brands
        entities = []
        score = 0
        for entity in doc.ents:
            entities.append(str(entity))

        for entity in entities:
            if entity in item["brand"]:
                score += 10

        tokens = [str(token.text) for token in doc]
        # If we know any entities, exclude them, or we'll pick up all products mentioning brands too
        tokens = [t for t in tokens if t not in entities]

        # Execute an ANDed search, so we don't return OR items
        for token in doc:
            if str(token.text) in item["name"]:
                score += 8

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
    parser.add_argument(
        "--json", "-j",
        required=False,
        default=False,
        dest="json",
        action="store_true",
        help="Output data as json"
    )

    args = parser.parse_args()

    data = load_data(Path(args.data))

    # Relink up search term (we might want to reprocess it)
    search_term = " ".join(args.search)

    # Batch process the search
    results = batch_search(search_term, data, nlp_search, 10000)

    # Perform a cut to get rid of extrandeous results
    results = [r for r in results if r.score > 10]

    # Sort the actual results
    results.sort(reverse=True, key=lambda x: x.score)

    if not args.json:
        for result in results:
            print(result)
    else:
        print(json.dumps([res.data for res in results]))
