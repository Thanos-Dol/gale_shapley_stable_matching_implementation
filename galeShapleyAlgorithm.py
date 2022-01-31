import re as regex
import random

# format for input must be like: <group1canditate>([whitespace]:[whitespace]<group2canditate>[whitespace],
# [whitespace]<group2canditate>)+
#file = open('/home/n0mad/Documents/inputForStableMatching', 'r')
#data = file.readlines()
#nameindex = 0


class stableMatching:

    def __init__(self, groupa, groupb, groupapreferences=None, groupbpreferences=None):
        if isinstance(groupa, list):
            self.groupa = groupa
            lengthguard = len(groupa)
        else:
            self.groupa = None
            lengthguard = None

        if isinstance(groupb, list):
            if lengthguard != len(groupb):
                lengthguard = None
                self.groupa = None
                self.groupb = None
            else:
                self.groupb = groupb
        else:
            lengthguard = None
            self.groupa = None
            self.groupb = None
        self.participantsnumber = lengthguard
        self.groupapreferences = groupapreferences
        self.groupbpreferences = groupbpreferences

    def randomisepreferences(self, canditates) -> list:
        preferences = []
        if canditates:
            for i in range(self.participantsnumber):
                preference = []
                templist = canditates.copy()
                while templist:
                    preference.append(templist.pop(random.randint(0, len(templist) - 1)))
                preferences.append(preference)
        else:
            preferences = None
        return preferences

    def printpreferences(self):
        if self.groupapreferences is not None:
            index = 0
            for preferencelist in self.groupapreferences:
                print(self.groupa[index], end=': ')
                index += 1
                fullpreferenceline = ''
                for preferencename in preferencelist:
                    fullpreferenceline = fullpreferenceline + preferencename + ', '
                print(fullpreferenceline[:-2], end='\n')
            print()
        else:
            print('There is not preference list for group a', end='\n\n')

        if self.groupbpreferences is not None:
            index = 0
            for preferencelist in self.groupbpreferences:
                print(self.groupb[index], end=': ')
                index += 1
                fullpreferenceline = ''
                for preferencename in preferencelist:
                    fullpreferenceline = fullpreferenceline + preferencename + ', '
                print(fullpreferenceline[:-2], end='\n')
            print()
        else:
            print('There is not preference list for group b', end='\n\n')

    def stablematchingfinder(self):
        if self.participantsnumber is not None and self.groupapreferences is not None and self.groupbpreferences is not None:
            groupamatches = dict.fromkeys(self.groupa, None)
            groupbmatches = dict.fromkeys(self.groupb, None)
            groupbpreferenceshashed = [dict(zip(preference, range(self.participantsnumber))) for preference in self.groupbpreferences]
            matched = 0
            turnofgroupa = 0
            preferenceindexgroupa = [0 for i in range(self.participantsnumber)]
            while matched < self.participantsnumber:
                if turnofgroupa == self.participantsnumber:
                    turnofgroupa = 0
                if preferenceindexgroupa[turnofgroupa] is None:
                    offerer = self.groupa[turnofgroupa]
                    offered = self.groupapreferences[turnofgroupa][preferenceindexgroupa[turnofgroupa]]
                    if groupbmatches[offered] is None:
                        groupbmatches[offered] = offerer
                        groupamatches[offerer] = offered
                    else:
                        if groupbpreferenceshashed
                if preferenceindexgroupa[turnofgroupa] < self.participantsnumber:
