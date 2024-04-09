### TASK TWO -- TDD ###


"""
Let's write a test for our function first and then will write an actual code to ensure that
all tests pass.

Task
Given a list of dictionaries where keys are student's  name and student's mark.
calculate the average score for the exam.

If mark is not within the range 1 to 10, raise an error
Some mark values can be integers and some are strings, we need to process both
If mark is missing, use value 5

"""

from unittest import mock
from unittest import TestCase, main
from practice import average_exam_score, increment_line_number


class TestAverageExamScore(TestCase):

    def test_calculate_average(self):
        my_input = [
            {'name': 'Jane', 'mark': 7},
            {'name': 'Nitesh', 'mark': 6},
            {'name': 'Aisha', 'mark': 8},
            {'name': 'Zac', 'mark': 8},
        ]

        expected = 7.25

        result = average_exam_score(my_input)
        self.assertEqual(expected, result)

    def test_calculate_average_error_raised(self):
        my_input = [
            {'name': 'Jane', 'mark': 15},
            {'name': 'Nitesh', 'mark': 6},
            {'name': 'Aisha', },
            {'name': 'Zac', 'mark': 8},
        ]

        with self.assertRaises(ValueError):
            average_exam_score(my_input)


class TestIncrementLineNumber(TestCase):

    @mock.patch('practice.get_file_content')
    def test_mock_file_read_function(self, mock_get_file_content):
        content = [
            '1. Hello',
            '2. Hi',
            '3. Good morning',
        ]
        mock_get_file_content.return_value = content

        self.assertEqual(
            increment_line_number('some_file'),
            4
        )


if __name__ == '__main__':
    main()
