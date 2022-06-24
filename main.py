class BoardingThePlane(object):
    def __init__(self):
        self.dict_of_places = {0: 'A', 1: 'B', 2: 'C', 4: 'D', 5: 'E', 6: 'F'}
        self.delta = 0

    def put_in_places(self):
        seats, groups_parameters = self.__data_entry()
        for group in groups_parameters:
            is_sitting = False

            for row in range(len(seats)):
                if is_sitting:
                    break

                for seat in self.__get_side_range(group):
                    if is_sitting:
                        break

                    if seats[row][seat] == '.' and int(group[0]) == 1:
                        seats[row][seat] = 'X'
                        self.__print_info(row, seat, seats, group[0])
                        seats[row][seat] = '#'
                        is_sitting = True
                    elif seats[row][seat] == '.' and seats[row][seat + self.delta] == '.' and int(group[0]) == 2:
                        seats[row][seat] = 'X'
                        seats[row][seat + self.delta] = 'X'
                        self.__print_info(row, seat, seats, group[0])
                        seats[row][seat] = '#'
                        seats[row][seat + self.delta] = '#'
                        is_sitting = True
                    elif seats[row][seat] == '.' and seats[row][seat + self.delta] == '.' \
                            and seats[row][seat + self.delta] == '.' and int(group[0]) == 3:
                        seats[row][seat] = 'X'
                        seats[row][seat + self.delta] = 'X'
                        seats[row][seat + 2 * self.delta] = 'X'
                        self.__print_info(row, seat, seats, group[0])
                        seats[row][seat] = '#'
                        seats[row][seat + self.delta] = '#'
                        seats[row][seat + 2 * self.delta] = '#'
                        is_sitting = True
                    break
            if not is_sitting:
                print('Cannot fulfill passengers requirements')

    def __print_info(self, row, seat, seats, number_of_people):
        list_of_letters = []
        if int(number_of_people) == 1:
            list_of_letters.append(self.dict_of_places[seat])
            print(f'Passengers can take seats: {row + 1}{sorted(list_of_letters)[0]}')

        elif int(number_of_people) == 2:
            list_of_letters.append(self.dict_of_places[seat])
            list_of_letters.append(self.dict_of_places[seat + self.delta])
            print(
                f'Passengers can take seats: {row + 1}{sorted(list_of_letters)[0]}'
                f' {row + 1}{sorted(list_of_letters)[1]}')

        elif int(number_of_people) == 3:
            list_of_letters.append(self.dict_of_places[seat])
            list_of_letters.append(self.dict_of_places[seat + self.delta])
            list_of_letters.append(self.dict_of_places[seat + 2 * self.delta])
            print(
                f'Passengers can take seats: {row + 1}{sorted(list_of_letters)[0]} '
                f'{row + 1}{sorted(list_of_letters)[1]} '
                f'{row + 1}{sorted(list_of_letters)[2]}')
        else:
            raise Exception(f'Incorrect number of people. Only "1" or "2" or "3" params are available.')

        for lines in seats:
            print(''.join(lines))

    def __get_side_range(self, group):
        if group[1] == 'left':
            if group[2] == 'window':
                self.delta = 1
                return range(3)
            elif group[2] == 'aisle':
                self.delta = -1
                return range(2, -1, -1)
            else:
                raise Exception(f'Incorrect desired place. Only "window" or "aisle" params are available.')

        elif group[1] == 'right':
            if group[2] == 'window':
                self.delta = -1
                return range(6, 3, -1)
            elif group[2] == 'aisle':
                self.delta = 1
                return range(4, 7)
            else:
                raise Exception(f'Incorrect side. Only "left" or "right" params are available.')

    @staticmethod
    def __data_entry():
        rows = int(input())
        seats = []
        for i in range(rows):
            seats.append(list(input()))

        number_of_groups = int(input())
        groups_parameters = []
        for i in range(number_of_groups):
            groups_parameters.append((input().split(' ')))

        return seats, groups_parameters


if __name__ == '__main__':
    a = BoardingThePlane()
    a.put_in_places()
