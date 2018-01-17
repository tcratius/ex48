import pytest
from ex48.lexicon import Lexicon as lexicon


@pytest.mark.parametrize("test_input, expected_output", 
                     [

                     ("north",[('direction', 'north')]),
                     ("south",[('direction', 'south')]),
                     ("east",[('direction', 'east')]),
                     ("eat",[('verb', 'eat')]),
                     ("kill",[('verb', 'kill')]),
                     ("the",[('stop', 'the')]),
                     ("in",[('stop', 'in')]),
                     ("bear",[('noun', 'bear')]),
                     ("princess",[('noun', 'princess')]),
                     ("ASDFAD",[('error', 'ASDFAD')]),
                     ("1234",[('number', 1234)]),
                     ("kronor",[('money', 'kronor')]),
                     ("meter",[('distance', 'meter')]),

                     ]
                    )

def test_all(test_input, expected_output):
    test = lexicon()
    all = test.scan(test_input)
    assert all == expected_output



