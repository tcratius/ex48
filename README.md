# ex48

Making a lexicon tuple and using a lexicon_tests.py file to test it.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

- python 2.7 
- nosetests 
- pytest

### Installing

Both python, nose tests and pytest will need to be installed for your various systems i.e. windows, mac, linux, google.

## Running the tests

To use pytest with nosetests

```
doc.pytest.org/en/latest/nose.html
```
To test lexicon.py goto to file ex48/tests in terminal and run

```
pytest lexicon_tests.py
```


### Break down into end to end tests

The lexicon scan was built off the lexicon_test.py file as on page 232

```
    def test_directions():
        assert_equal(lexicon.scan(”north”), [(’direction’, ’north’)])
        result = lexicon.scan(”north south east”)
        assert_equal(result, [(’direction’, ’north’),
                              (’direction’, ’south’),
                              (’direction’, ’east’)])

```
## Acknowledgments

* Inpired by 

