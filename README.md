# Given any number up to a vigintillion, this class will return the same number in words

## requirements
- python3 

## running the tests
```python tests.py```

## using custom tests
```
Import NumbersToWords;
NumbersToWords("45781", add_and=False).words # for when the conjuntion "and" is unnecessary
NumbersToWords("45781", add_and=True).words # for when the conjuntion "and" is necessary

# replace 45781 with custom numbers as desired within the bounds
```

## Assumptions
The class only works with strings. We are not handling
- negative integers
- direct integers. 

You have to pass the number intented as a string
Of course a serializer can be used to validate this in production
if it was user input.

##With text to speech 

crete a virtual env with pyhton 3 

