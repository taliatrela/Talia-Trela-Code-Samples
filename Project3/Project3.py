import os
import math
from StacksAndQueues import MyStack, CircularQueue
#  The stack and queue classes were made together as a class, so they are from my professor's GitHub Account:
#  https://raw.githubusercontent.com/EricCharnesky/CIS2001-Winter2019/master/Week5/Week5.py


class Plane:
    def __init__(self, plane_number, num_items_to_load):
        self.plane_number = plane_number
        self.num_items_to_load = num_items_to_load
        self.num_items_loaded = 0
        self.loading_time = 0


class Train:
    def __init__(self, train_number, num_items_to_load):
        self.train_number = train_number
        self.num_items_to_load = num_items_to_load
        self.num_items_loaded = 0
        self.loading_time = 0


class Dock:
    TIME_CONSTANT_TO_TRAVEL_TO_TRAIN_AND_BACK = 2
    TIME_CONSTANT_TO_TRAVEL_TO_PLANE_AND_BACK = 10

    def __init__(self):
        self._queue_of_stacks_going_to_train = CircularQueue()
        self._queue_going_to_plane = CircularQueue()
        self._planes = []
        self._trains = []

    def _stack_train_items_into_queue(self, load_sequence):
        num_stacks_needed = math.ceil((len(load_sequence) / 5))
        index = 0
        for n in range(num_stacks_needed):
            new_stack = MyStack()
            while len(new_stack) < 5:
                new_stack.push(load_sequence[index])
                index += 1
                if index >= len(load_sequence):
                    break
            self._queue_of_stacks_going_to_train.enqueue(new_stack)

    def _place_plane_items_on_assembly_line(self, load_sequence):
        for item in load_sequence:
            self._queue_going_to_plane.enqueue(item)

    def find_loading_times_for_trains(self):
        while not self._queue_of_stacks_going_to_train.is_empty():
            load_stack = self._queue_of_stacks_going_to_train.dequeue()
            while len(load_stack) > 0:
                item = load_stack.pop()
                for train in self._trains:
                    if train.num_items_loaded != train.num_items_to_load:
                        train.loading_time += (item * Dock.TIME_CONSTANT_TO_TRAVEL_TO_TRAIN_AND_BACK)
                        # Only add time if train is not already loaded.
                        if item == train.train_number:
                            train.num_items_loaded += 1
        for train in self._trains:
            if train.num_items_loaded > 0:  # Only subtract time if it actually had items loaded.
                train.loading_time -= ((Dock.TIME_CONSTANT_TO_TRAVEL_TO_TRAIN_AND_BACK / 2) * train.train_number)
                # Must subtract half of the time it takes to travel there and back for each train, since it can leave
                # when it is fully loaded.
        return

    def find_loading_times_for_planes(self):
        while not self._queue_going_to_plane.is_empty():
            item_unloaded = self._queue_going_to_plane.dequeue()
            for plane in self._planes:
                if plane.num_items_loaded != plane.num_items_to_load:
                    plane.loading_time += (item_unloaded * Dock.TIME_CONSTANT_TO_TRAVEL_TO_PLANE_AND_BACK)
                    if item_unloaded == plane.plane_number:
                        plane.num_items_loaded += 1

        for plane in self._planes:
            if plane.num_items_loaded > 0:  # Only subtract time if it actually had items loaded.
                plane.loading_time -= ((Dock.TIME_CONSTANT_TO_TRAVEL_TO_PLANE_AND_BACK / 2) * plane.plane_number)
            # Again, must subtract half of the time it takes to travel there and back for each plane, since it can leave
            # when it is fully loaded.
        return

    def prepare_planes_trains_and_loads_from_file(self, file):
        with open(file) as myfile:
            num_trains, num_planes, num_items_for_trains, num_items_for_planes = \
                [int(num) for num in myfile.readline().split()]

            train_items = [int(num) for num in myfile.readline().split()]
            for index in range(num_trains):
                self._trains.append(Train((index + 1), train_items[index]))

            plane_items = [int(num) for num in myfile.readline().split()]
            for index in range(num_planes):
                self._planes.append(Plane((index + 1), plane_items[index]))

            train_load_sequence = [int(num) for num in myfile.readline().split()]
            plane_load_sequence = [int(num) for num in myfile.readline().split()]

        self._stack_train_items_into_queue(train_load_sequence)
        self._place_plane_items_on_assembly_line(plane_load_sequence)

    def reset(self):
        self._queue_of_stacks_going_to_train = CircularQueue()
        self._queue_going_to_plane = CircularQueue()
        self._planes = []
        self._trains = []

    def print_train_times(self):
        if len(self._trains) > 0:
            for index in range(len(self._trains)):
                if index != (len(self._trains) - 1):
                    print(int(self._trains[index].loading_time), end=' ')
                else:
                    print(int(self._trains[index].loading_time))
        else:
            print()
            # Print a blank line if there are no trains.

    def print_plane_times(self):
        if len(self._planes) > 0:
            for index in range(len(self._planes)):
                if index != (len(self._planes) - 1):
                    print(int(self._planes[index].loading_time), end=' ')
                else:
                    print(int(self._planes[index].loading_time))
        else:
            print()
            # Print a blank line if there are no planes.


def print_loading_times_of_a_given_file(file, dock):
    dock.reset()
    print("File:", file)
    dock.prepare_planes_trains_and_loads_from_file(file)
    dock.find_loading_times_for_trains()
    dock.find_loading_times_for_planes()
    dock.print_train_times()
    dock.print_plane_times()


# Output for input files 1 - 8:
if __name__ == '__main__':
    my_dock = Dock()
    for num in range(1,9):
        print_loading_times_of_a_given_file('Inputs{}input{}.txt'.format(os.path.sep, num), my_dock)
        print()












