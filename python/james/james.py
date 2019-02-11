import unittest
import random
import asyncio

from time import sleep
from unittest import mock
from datetime import datetime, timedelta


class Grid():

    def __init__(self):
        self.grid_size = 3

    @property
    def map(self):
        return [[]] * (self.grid_size * self.grid_size)

    @property
    def middle(self):
        length = len(self.map)
        return int(length / 2)

    def update_grid_size(self, num):
        self.grid_size = num


class MoveException(Exception):
    pass


class Bot():
    name = 'James'
    grid = Grid()
    loc = grid.middle

    def __init__(self):
        self.tasks = []

    def location(self):
        return self.loc

    async def assign_task(self, task):
        seconds = random.randint(3, 5)
        print('On it! I will complete this task in {} seconds'.format(seconds))
        self.tasks.append({
            'time_until_complete': timedelta(seconds=seconds),
            'name': task
        })
        await self.complete_tasks()

    async def task(self, task):
        await asyncio.sleep(task['time_until_complete'].total_seconds())
        print('Task "{}" completed!'.format(task['name']))
        self.tasks.remove(task)

    async def gather_tasks(self):
        tasks = [self.task(t) for t in self.tasks]
        await asyncio.gather(*tasks)

    async def complete_tasks(self):
        asyncio.run(self.gather_tasks())

    def move(self, direction):
        directions = {
            'up': {'num': -3, 'invalid': self.loc < len(self.grid.map[:self.grid.grid_size])},
            'down': {'num': 3, 'invalid': self.loc > len(self.grid.map[:-self.grid.grid_size])},
            'right': {'num': 1, 'invalid': (self.loc + 1) % self.grid.grid_size == 0},
            'left': {'num': -1, 'invalid': (self.loc + 1) % self.grid.grid_size == 1}
        }
        try:
            if directions[direction]['invalid']:
                raise MoveException('There is nowhere for me to move {}'.format(direction))
            self.loc += directions[direction]['num']
        except KeyError:
            raise MoveException('I cannot move "{}". Please choose "up", "down" "left", or "right".'.format(direction))

    def how_long_since(self, date, format='days'):
        date_obj = datetime.strptime(date, '%Y/%m/%d')
        return self.format_date_difference(
            datetime.now() - date_obj, date, format, 'It has been {since:,} {format} since {date}')

    def how_long_until(self, date, format='days'):
        date_obj = datetime.strptime(date, '%Y/%m/%d')
        return self.format_date_difference(date_obj - datetime.now(), date, format, '{date} is {since:,} {format} away')

    def format_date_difference(self, difference, date, format, return_str):
        since = difference.days
        if format == 'years':
            since = round(since / 365.2425)
        return return_str.format(date=date, since=since, format=format)

    def display_location(self):
        grid_str = ''
        for idx, spot in enumerate(self.grid.map):
            if idx == self.location():
                grid_str += ' J '
            else:
                grid_str += ' _ '
            if idx in [2, 5]:
                grid_str += '\n'
        return grid_str


class GridTests(unittest.TestCase):

    def test_finds_middle_of_default_map(self):
        grid = Grid()
        self.assertEqual(4, grid.middle)

    def test_find_middle_of_expanded_grid(self):
        grid = Grid()
        grid.update_grid_size(17)
        self.assertEqual(144, grid.middle)

    def test_find_middle_of_even(self):
        grid = Grid()
        grid.update_grid_size(8)
        self.assertEqual(32, grid.middle)

    def test_can_expand_grid_squarely(self):
        grid = Grid()
        self.assertEqual(9, len(grid.map))
        grid.update_grid_size(20)
        self.assertEqual(400, len(grid.map))

    def test_can_decrease_size_of_grid_squarely(self):
        grid = Grid()
        self.assertEqual(9, len(grid.map))
        grid.update_grid_size(2)
        self.assertEqual(4, len(grid.map))


class JamesTests(unittest.TestCase):

    def test_displays_james_default_location_in_grid(self):
        expected = ' _  _  _ \n _  J  _ \n _  _  _ '
        james = Bot()
        self.assertEqual(expected, james.display_location())

    def test_james_can_move_location_up(self):
        james = Bot()
        self.assertEqual(4, james.location())
        james.move('up')
        self.assertEqual(1, james.location())
        expected = ' _  J  _ \n _  _  _ \n _  _  _ '
        self.assertEqual(expected, james.display_location())

    def test_james_can_move_location_down(self):
        james = Bot()
        self.assertEqual(4, james.location())
        james.move('down')
        self.assertEqual(7, james.location())
        expected = ' _  _  _ \n _  _  _ \n _  J  _ '
        self.assertEqual(expected, james.display_location())

    def test_james_can_move_location_right(self):
        james = Bot()
        self.assertEqual(4, james.location())
        james.move('right')
        self.assertEqual(5, james.location())
        expected = ' _  _  _ \n _  _  J \n _  _  _ '
        self.assertEqual(expected, james.display_location())

    def test_james_can_move_location_left(self):
        james = Bot()
        self.assertEqual(4, james.location())
        james.move('left')
        self.assertEqual(3, james.location())
        expected = ' _  _  _ \n J  _  _ \n _  _  _ '
        self.assertEqual(expected, james.display_location())

    def test_james_raises_exception_when_there_it_is_not_possible_to_move_left(self):
        james = Bot()
        self.assertEqual(4, james.location())
        james.move('left')
        with self.assertRaises(MoveException) as e:
            james.move('left')
        self.assertEqual(str(e.exception), 'There is nowhere for me to move left')

    def test_james_raises_exception_when_there_it_is_not_possible_to_move_right(self):
        james = Bot()
        self.assertEqual(4, james.location())
        james.move('right')
        with self.assertRaises(MoveException) as e:
            james.move('right')
        self.assertEqual(str(e.exception), 'There is nowhere for me to move right')

    def test_james_raises_exception_when_there_it_is_not_possible_to_move_down(self):
        james = Bot()
        self.assertEqual(4, james.location())
        james.move('down')
        with self.assertRaises(MoveException) as e:
            james.move('down')
        self.assertEqual(str(e.exception), 'There is nowhere for me to move down')

    def test_james_raises_exception_when_there_it_is_not_possible_to_move_up(self):
        james = Bot()
        self.assertEqual(4, james.location())
        james.move('up')
        with self.assertRaises(MoveException) as e:
            james.move('up')
        self.assertEqual(str(e.exception), 'There is nowhere for me to move up')

    def test_move_error_raised_if_invalid_direction_supplied_to_move_method(self):
        james = Bot()
        with self.assertRaises(MoveException) as e:
            james.move('diagonal')
        self.assertEqual(str(e.exception), 'I cannot move "diagonal". Please choose "up", "down" "left", or "right".')

    def test_can_tell_how_long_ago_a_date_was_in_days(self):
        james = Bot()
        since = datetime.now() - datetime(1994, 9, 28)
        self.assertEqual(
            'It has been {:,} days since 1994/09/28'.format(since.days),
            james.how_long_since('1994/09/28', 'days')
        )

    def test_can_tell_how_long_ago_a_date_was_in_years(self):
        james = Bot()
        difference = datetime.now() - datetime(1994, 9, 28)
        since = round(difference.days / 365.2425)
        self.assertEqual(
            'It has been {:,} years since 1994/09/28'.format(since),
            james.how_long_since('1994/09/28', 'years')
        )

    def test_can_tell_how_long_until_a_date_was_in_days(self):
        james = Bot()
        since = datetime(2104, 9, 28) - datetime.now()
        self.assertEqual(
            '2104/09/28 is {:,} days away'.format(since.days),
            james.how_long_until('2104/09/28', 'days')
        )

    def test_can_tell_how_long_until_a_date_was_in_years(self):
        james = Bot()
        difference = datetime(2104, 9, 28) - datetime.now()
        since = round(difference.days / 365.2425)
        self.assertEqual(
            '2104/09/28 is {:,} years away'.format(since),
            james.how_long_until('2104/09/28', 'years')
        )

    def test_can_assign_task(self):
        james = Bot()
        james.assign_task('Wash dishes')
        self.assertEqual(james.tasks[0]['name'], 'Wash dishes')

    def test_is_completed_after_time_to_complete(self):
        james = Bot()
        with mock.patch.object(random, 'randint', return_value=10):
            james.assign_task('Wash dishes')
            self.assertEqual(james.tasks[0]['time_until_complete'], timedelta(seconds=10))

    def test_task_is_removed_once_completed(self):
        james = Bot()
        with mock.patch.object(random, 'randint', return_value=1):
            james.assign_task('Wash dishes')
        james.complete_tasks()
        self.assertEqual(james.tasks, [])
