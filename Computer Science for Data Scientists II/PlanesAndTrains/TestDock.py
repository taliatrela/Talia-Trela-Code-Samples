import os
from unittest import TestCase
from Project3 import Dock, Plane, Train
from StacksAndQueues import MyStack, CircularQueue


class TestDock(TestCase):
    def test___init__(self):
        # Arrange
        expected_length_of_queue_of_stacks = 0
        expected_length_of_queue = 0
        expected_num_trains = 0
        expected_num_planes = 0

        # Act
        my_dock = Dock()

        # Assert
        self.assertEqual(len(my_dock._queue_of_stacks_going_to_train), expected_length_of_queue_of_stacks)
        self.assertEqual(len(my_dock._queue_going_to_plane), expected_length_of_queue)
        self.assertEqual(len(my_dock._trains), expected_num_trains)
        self.assertEqual(len(my_dock._planes), expected_num_planes)

    def test_place_plane_items_on_assembly_line(self):
        # Arrange
        load_sequence = [2, 1, 1, 2, 1]
        expected_queue = CircularQueue()
        for item in load_sequence:
            expected_queue.enqueue(item)

        # Act
        my_dock = Dock()
        my_dock._place_plane_items_on_assembly_line(load_sequence)

        # Assert

        self.assertEqual(my_dock._queue_going_to_plane, expected_queue)

    def test_stack_train_items_into_queue(self):
        # Arrange
        load_sequence = [2, 2, 2, 1, 3, 2, 2, 2, 1, 2]
        expected_queue = CircularQueue()
        stack1 = MyStack()
        stack1.push(2)
        stack1.push(2)
        stack1.push(2)
        stack1.push(1)
        stack1.push(3)
        stack2 = MyStack()
        stack2.push(2)
        stack2.push(2)
        stack2.push(2)
        stack2.push(1)
        stack2.push(2)

        expected_queue.enqueue(stack1)
        expected_queue.enqueue(stack2)

        # Act
        my_dock = Dock()
        my_dock._stack_train_items_into_queue(load_sequence)

        # Assert

        self.assertEqual(my_dock._queue_of_stacks_going_to_train, expected_queue)

    def test_reset(self):
        # Arrange
        my_dock = Dock()
        my_dock.prepare_planes_trains_and_loads_from_file('Inputs{}input1.txt'.format(os.path.sep))
        my_dock.find_loading_times_for_trains()
        my_dock.find_loading_times_for_planes()

        # Act
        my_dock.reset()

        # Assert
        self.assertEqual(len(my_dock._queue_of_stacks_going_to_train), 0)
        self.assertEqual(len(my_dock._queue_going_to_plane), 0)
        self.assertEqual(len(my_dock._trains), 0)
        self.assertEqual(len(my_dock._planes), 0)

    def test_find_loading_times_for_trains(self):
        # Arrange
        my_dock = Dock()
        for num in range(1, 9):
            my_dock.reset()
            my_dock.prepare_planes_trains_and_loads_from_file('Inputs{}input{}.txt'.format(os.path.sep, num))
            # Act
            my_dock.find_loading_times_for_trains()
            with open('Outputs{}output{}.txt'.format(os.path.sep, num)) as myfile:
                train_times = myfile.readline().split()
            index = 0

            # Assert
            for train in my_dock._trains:
                self.assertEqual(int(train.loading_time), int(train_times[index]))
                index += 1

    def test_find_loading_times_for_planes(self):
        # Arrange
        my_dock = Dock()
        for num in range(1, 9):
            my_dock.reset()
            my_dock.prepare_planes_trains_and_loads_from_file('Inputs{}input{}.txt'.format(os.path.sep, num))
            # Act
            my_dock.find_loading_times_for_planes()
            with open('Outputs{}output{}.txt'.format(os.path.sep, num)) as myfile:
                myfile.readline()
                plane_times = myfile.readline().split()
            index = 0

            # Assert
            for plane in my_dock._planes:
                self.assertEqual(int(plane.loading_time), int(plane_times[index]))
                index += 1

    def test_prepare_planes_trains_and_loads_from_file(self):
        # Arrange
        expected_num_trains = 3
        expected_num_planes = 2
        expected_train_1 = Train(1, 2)
        expected_train_2 = Train(2, 7)
        expected_train_3 = Train(3, 1)
        expected_plane_1 = Plane(1, 3)
        expected_plane_2 = Plane(2, 2)

        expected_queue_for_train_items = CircularQueue()
        stack1 = MyStack()
        stack1.push(2)
        stack1.push(2)
        stack1.push(2)
        stack1.push(1)
        stack1.push(3)
        stack2 = MyStack()
        stack2.push(2)
        stack2.push(2)
        stack2.push(2)
        stack2.push(1)
        stack2.push(2)

        expected_queue_for_train_items.enqueue(stack1)
        expected_queue_for_train_items.enqueue(stack2)

        # Arrange
        load_sequence_for_planes = [2, 1, 1, 2, 1]
        expected_queue_going_to_plane = CircularQueue()
        for item in load_sequence_for_planes:
            expected_queue_going_to_plane.enqueue(item)


        # Act
        my_dock = Dock()
        my_dock.prepare_planes_trains_and_loads_from_file('Inputs{}input1.txt'.format(os.path.sep))

        # Assert
        self.assertEqual(len(my_dock._trains), expected_num_trains)
        self.assertEqual(len(my_dock._planes), expected_num_planes)
        self.assertEqual(my_dock._trains[0].num_items_to_load, expected_train_1.num_items_to_load)
        self.assertEqual(my_dock._trains[1].num_items_to_load, expected_train_2.num_items_to_load)
        self.assertEqual(my_dock._trains[2].num_items_to_load, expected_train_3.num_items_to_load)
        self.assertEqual(my_dock._planes[0].num_items_to_load, expected_plane_1.num_items_to_load)
        self.assertEqual(my_dock._planes[1].num_items_to_load, expected_plane_2.num_items_to_load)

        self.assertEqual(my_dock._queue_going_to_plane, expected_queue_going_to_plane)
        self.assertEqual(my_dock._queue_of_stacks_going_to_train, expected_queue_for_train_items)


class TestPlane(TestCase):
    def test__init__(self):
        # Arrange
        plane_number = 1
        num_items_to_load = 7

        # Act
        my_plane = Plane(plane_number, num_items_to_load)

        # Assert
        self.assertEqual(my_plane.plane_number, plane_number)
        self.assertEqual(my_plane.num_items_to_load, num_items_to_load)
        self.assertEqual(my_plane.num_items_loaded, 0)
        self.assertEqual(my_plane.loading_time, 0)


class TestTrain(TestCase):
    def test__init__(self):
        # Arrange
        train_number = 1
        num_items_to_load = 7

        # Act
        my_train = Train(train_number, num_items_to_load)

        # Assert
        self.assertEqual(my_train.train_number, train_number)
        self.assertEqual(my_train.num_items_to_load, num_items_to_load)
        self.assertEqual(my_train.num_items_loaded, 0)
        self.assertEqual(my_train.loading_time, 0)

