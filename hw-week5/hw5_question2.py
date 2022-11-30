from abc import ABC
from typing import Any, List, Callable, OrderedDict

class preference_profile(ABC):
    @classmethod
    def sum_of_scores(self, preferences) -> dict:
        """
        Construct and returns a dict structure. Used at the initialization phase of an algorithm.
        """
        raise NotImplementedError("Choose a specific input type")

    @classmethod
    def create_empty_dict(self, preferences)-> dict:
        """
        Create a candidate dict, without scores.
        """
        raise NotImplementedError("Choose a specific input type")

    @classmethod
    def add_ballot(self, preferences: dict, ballot)-> dict:
        """
        Add the given ballot to the preferences.
        """
        raise NotImplementedError("Choose a specific input type")

class scores_dict(preference_profile):
    """ Input of a dict of candidates and their scores.  """
    @classmethod
    def create_empty_dict(self, preferences:dict)-> dict:
        """
        Create a candidate dict, without scores.
        """
        scores = {}
        for c in preferences.keys():
            scores[c] = 0
        return scores

    @classmethod
    def create_current_score(self, preferences:dict) -> dict:
        return preferences

    @classmethod
    def add_ballot(self, preferences: dict, ballot:dict)-> dict:
        """
        Add the given ballot to the preferences.
        """
        for c in preferences.keys():
            preferences[c] += ballot[c]
        return preferences

class list_of_preferences(preference_profile):
    """ Input of a dict of candidates and their scores.  """
    @classmethod
    def create_empty_dict(preferences:list)-> dict:
        """
        Create a candidate dict, without scores.
        """
        scores = {}
        for key in preferences[0]:
            scores[key] = 0
        return scores

    @classmethod
    def create_current_score(preferences:list) -> dict:
        scores = list_of_preferences.create_empty_dict(preferences)
        for b in preferences:
            scores = list_of_preferences.add_ballot(scores, b)
        return scores

    @classmethod
    def add_ballot(preferences: dict, ballot:list)-> dict:
        """
        Add the given ballot to the preferences.
        """
        for i in range(len(ballot)):
            preferences[ballot[i]] += len(ballot) - 1 - i
        return preferences

class OutputType(ABC):
    @classmethod
    def create_output(self,scores: dict, *args):
        """
        Construct and return a preference structure. Used at the initialization phase of an algorithm.
        """
        raise NotImplementedError("Choose a specific output type")

    @classmethod
    def add_score(self, candidate, score:int):
        """
        Adds a candidate and its' score to the preference order.
        """
        raise NotImplementedError("Choose a specific output type")

    @classmethod
    def extract_output(self):
        """
        Return the required output from the given preference structure.
        """
        raise NotImplementedError("Choose a specific output type")


class manipulation(OutputType):
    """ Output if the manipulation is successfull or not.  """
    scores = {}
    @classmethod
    def create_output(self, scores: dict, *args) -> dict:
        self.scores = scores

    @classmethod
    def add_score(self, candidate, score:int) -> dict:
        """
        Adds a candidate and its' score to the preference order.
        """
        self.scores[candidate] += score
        return self.scores
        
    @classmethod
    def extract_output(self) -> str:
        return "Manipulation is successful."

class manipulation_preferences(manipulation):
    """ Output the list of sums of all bins (but not the bins' contents).  """
    manipulators = []
    manipulators_dict = {}
    scores = {}
    @classmethod
    def create_output(self, scores: dict, k: int) -> List:
        self.manipulators = []
        self.manipulators_dict = {}
        m = len(scores)
        for i in range(k):
            self.manipulators.append([" "])
            for j in range(m-1):
                self.manipulators[i].append(" ")
        for i in range(len(scores)):
            self.manipulators_dict[i] = 0
        self.scores = scores

    @classmethod
    def add_score(self, candidate, score:int):
        """
        Adds a candidate and its' score to the preference order.
        """
        self.scores[candidate] += score
        s = self.manipulators_dict[score]
        self.manipulators_dict[score] += 1
        self.manipulators[s][score] = candidate 
        return self.scores

    @classmethod
    def extract_output(self) -> str: #List: change the function for a correct manipulation
        return "Relaxed manipulation: "+str(self.manipulators)

def largest_fit(candidate, k: int, scores: dict, output: OutputType):
    """
    Finds a manipulation with the largest fit algorithm, if possible.    
    """
    candidates = {c:0 for c in scores.keys()}
    m = len(scores)
    for i in range(k):
        scores = output.add_score(candidate, m-1)
    for c in scores:
        if scores[c] > scores[candidate]:
            return False
    gap = OrderedDict()
    for c in scores.keys():
        if c != candidate:
            gap[c] = scores[candidate] - scores[c]
            if gap[c] < 0:
                return False
    for i in range(m - 2, -1, -1):
        for j in range(k, 0, -1):
            for c,v in sorted(gap.items(), key=lambda item: item[1], reverse = True):
                if v - i < 0: 
                    return False
                elif candidates[c]<k:
                    gap[c] = v - i
                    scores = output.add_score(c, i)
                    candidates[c] += 1
                    break
    return True        






def average_fit(candidate, k: int, scores: dict, output: OutputType):
    """
    Finds a manipulation with the average fit algorithm, if possible.    
    """
    candidates = {c:0 for c in scores.keys()}
    m = len(scores)
    for i in range(k):
        output.add_score(candidate, m-1)
    for c in scores:
        if scores[c] > scores[candidate]:
            return False
    gap = OrderedDict()
    for c in scores.keys():
        if c != candidate:
            gap[c] = (scores[candidate] - scores[c])/k
            if gap[c] < 0:
                return False
    for i in range(m - 2, -1, -1):
        for j in range(k, 0, -1):
            sorted(gap.items(), key=lambda item: candidates[item[0]], reverse = True)
            for c,v in sorted(gap.items(), key=lambda item: item[1], reverse = True):
                if candidates[c]<k:
                    if scores[candidate] >= i + scores[c]:
                        scores = output.add_score(c, i)
                        candidates[c] += 1
                        gap[c] = (scores[candidate] - scores[c])/(k - candidates[c]) if candidates[c] < k else 0
                        break
    return True
    

def find_manipulation(algorithm: Callable, preferences, candidate, k: int, input: preference_profile, output: OutputType):
    """
    Finds a manipulation with the given algorithm, if possible.
    >>> find_manipulation(largest_fit,{'a':3,'b':4,'c':5,'d':0},'d',2,scores_dict,manipulation_preferences)
    "Relaxed manipulation: [['b', 'a', 'a', 'd'], ['c', 'c', 'b', 'd']]"
    >>> find_manipulation(largest_fit,{'a':3,'b':4,'c':5,'d':0},'d',2,scores_dict,manipulation)
    'Manipulation is successful.'
    >>> find_manipulation(average_fit,{'a':3,'b':4,'c':5,'d':0},'d',2,scores_dict,manipulation_preferences)
    "Relaxed manipulation: [['b', 'a', 'a', 'd'], ['c', 'c', 'b', 'd']]"
    >>> find_manipulation(average_fit,{'a':3,'b':4,'c':5,'d':0},'d',2,scores_dict,manipulation)
    'Manipulation is successful.'
    
    """

    scores = input.create_current_score(preferences)
    output.create_output(scores, k)
    ans = algorithm(candidate, k, scores, output)
    if ans:
        return output.extract_output()
    else:
        return "Manipulation failed."


print(find_manipulation(largest_fit,{'a':3,'b':4,'c':5,'d':0},'d',2,scores_dict,manipulation_preferences))
print(find_manipulation(largest_fit,{'a':3,'b':4,'c':5,'d':0},'d',2,scores_dict,manipulation))
print(find_manipulation(average_fit,{'a':3,'b':4,'c':5,'d':0},'d',2,scores_dict,manipulation_preferences))
print(find_manipulation(average_fit,{'a':3,'b':4,'c':5,'d':0},'d',2,scores_dict,manipulation))

if __name__ == "__main__":
    import doctest

    print(doctest.testmod())


