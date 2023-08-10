#!/usr/bin/python3
'''Minimum Operations.
'''


def minOperations(n):
    '''Calculates the fewest number.
    '''
    if not isinstance(n, int):
        return 0
    counter = 0
    clipboard = 0
    done = 1
    # print('H', end='')
    while done < n:
        if clipboard == 0:
            # init (the first copy all and paste)
            clipboard = done
            done += clipboard
            counter += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif n - done > 0 and (n - done) % done == 0:
            # copy all and paste
            clipboard = done
            done += clipboard
            counter += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif clipboard > 0:
            # paste
            done += clipboard
            counter += 1
            # print('-(01)->{}'.format('H' * done), end='')
    # print('')
    return counter
