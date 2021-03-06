# themarkovoffice
Check out [@TheMarkovOffice](https://twitter.com/TheMarkovOffice) to see the tweets generated by this code.

This twitter bot uses [markovify](https://github.com/jsvine/markovify).

## What does this bot do?
This bot uses a complete transcript of all nine seasons of the American version of *The Office* and separates each speaking part by character. It then has separate groups of text for each character, and generates hourly fictional vignettes using Markov chains from each character.

The characters are selected randomly, with some nuances to make the conversations flow a bit more naturally. Random selections rarely follow normal conversational patters like `Character A`, `Character B`, `Character A`, `Character B`. There are measures in place to encourage these sorts of typical exchanges instead of having several characters all chiming in.

Here are a few examples:
- https://twitter.com/TheMarkovOffice/status/1284800314332401665?s=20
- https://twitter.com/TheMarkovOffice/status/1292772839230181377?s=20
- https://twitter.com/TheMarkovOffice/status/1292591560794738688?s=20

## What is Markov Chaining?

Wikipedia's very dense definition:
> A [Markov Chain](https://en.wikipedia.org/wiki/Markov_chain) is a stochastic model describing a sequence of possible events in which the probability of each event depends only on the state attained in the previous event. 

In the context of a body of text, that means building a sentence where the next word is based on the previous n words, and nothing else.

For example, if you have a body of text that contains the following sentences:
- *"Your cat is orange"*
- *"I fed the cat this morning"*
- *"Nobody saw me this morning when I went to work"*

You may end up with a Markov Chained sentence like this: *"Your cat this morning when I went to work"*.

In this simplified example, the transition words of *cat* and *morning* represent opportunities for the chain to break from the existing sentence structure.

## Is this valuable?

Not really, but it's kind of fun, and it was an interesting project to work on. =D



