"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [5, 8, 13, 27, 14],
            "answer": 3
        },
        {
            "input": [1, 2, 3, 4, 100000],
            "answer": 99990
        }
    ],
    "Extra": [
        {
            "input": [2, 3, 5, 8, 13, 21],
            "answer": 0
        },
        {
            "input": [1111, 2222, 3333, 4444, 11111],
            "answer": 1
        },
	{
            "input": [1118, 2524, 11, 1990, 2, 1879],
            "answer": 214
        }
    ]
}
