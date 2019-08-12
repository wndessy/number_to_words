# This package will generate the English word equivalent of any given number upto a vigintillion

## requirements
- python3 

## installation
run the following pip command to install the latest version
```
pip install number-to-words
```

## usage

The following is an example of how to use the package

### add_and=True
- for when the conjuntion "and" is necessary in the wording of a number
```python

from number_to_words import NumbersToWords
in_words=NumbersToWords("281029292028020", add_and=True).words
print(in_words)

```

#### output
```bash
two hundred and eighty one trillion twenty nine billion two hundred and ninety two million twenty eight thousand and twenty
```
- for when the conjunction "and" is not necessary in the wording of a number

```python

from number_to_words import NumbersToWords
in_words=NumbersToWords("281029292028020", add_and=False).words
print(in_words)
```
#### output

```bash
two hundred eighty one trillion twenty nine billion two hundred ninety two million twenty eight thousand twenty
```

## Points to note 
- You have to pass the number intended as a string parameter
- The package does not handle the following yet:
    -  negative integers
    -  direct integers. (not converted to string)
    -  decimal numbers 
    
- replace 281029292028020 with custom numbers as desired within the bounds


## ENJOY!