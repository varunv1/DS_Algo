def tower_of_hanoi(no_of_discs, start_peg=1, end_peg=3):
    if no_of_discs:
        tower_of_hanoi(no_of_discs-1, start_peg, 6-start_peg-end_peg)
        print('Move disk %d from peg %d to peg %d' %
              (no_of_discs, start_peg, end_peg))
        tower_of_hanoi(no_of_discs-1, 6-start_peg-end_peg, end_peg)


tower_of_hanoi(3)
