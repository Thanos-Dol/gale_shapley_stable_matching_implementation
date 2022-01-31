# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import galeShapleyAlgorithm

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sm = galeShapleyAlgorithm.stableMatching(['mit', 'oxford', 'harvard', 'cambridge', 'california', 'john hopkins', 'barkley', 'coppehngaghe'], ['sabot', 'takahashi', 'abbott', 'steven', 'papu', 'remedi', 'dekahor', 'verejim'])
    sm.groupapreferences = sm.randomisepreferences(sm.groupb)
    sm.groupbpreferences = sm.randomisepreferences(sm.groupa)
    sm.printpreferences()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
