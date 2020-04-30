# Search Challenge

## Approach

So, I'm attempting to search through a json file of 70k, but the algorithm should be optimised to handle even larger sets.

I'm assuming that reading the data we read in from the JSON isn't part of the challenge (as JSON reads all the data into 
memory first, so a read of all that data probably would die).

The approach I'm going to take involves batch processing the data, which should keep the memory overheads down.  It also
means data could be supplied in batches too and the algorithms could be adapted easily.

I'm light on data science, so I'm not confident enough to use pandas and numpy in a timed setting (though I've used them).
I'm going to stick to python, which should be fine for this example.

I might try and see if I can work in some nlp, which I haven't had a chance to play with.

## Quickstart

Install:

`pip install -r requirements.pip`
`python -m spacy download en_core_web_sm`

Run:

'python search.py <search_terms> -d <data_dir> --json'

* search_term - the search you want to run
* -d/-data  - The data file (not required)
* -j/--json - Whether to output json (used mainly by the tests)


## Search Methods

**super_simple_search**:

This just splits the search term and looks up the terms.  It's basic and works, but has
lots of issues.  e.g. `Prada jumper` would return all jumpers

**nlp_search:**

Trying to use NLP to see if we can learn more about the search terms.  We use the spacy library for this.

Currently, we can pick out entities and check against brands for just those, which should help.  It
doesn't seem to pick out compound entities e.g. "Simply Be"

## Tests

I've tried to encode some of the searches into tests, just to have an idea of what it's doing.  These can be run by:

`python -m unittest test_search`