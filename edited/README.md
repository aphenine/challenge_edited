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

  