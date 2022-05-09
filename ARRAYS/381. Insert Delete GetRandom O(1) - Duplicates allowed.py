class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.d = defaultdict(set)
        

  '''
  RandomizedCollection is a data structure that contains a collection of numbers, possibly duplicates (i.e., a multiset). It should support inserting and removing specific elements and also removing a random element.

Implement the RandomizedCollection class:

RandomizedCollection() Initializes the empty RandomizedCollection object.
bool insert(int val) Inserts an item val into the multiset, even if the item is already present. Returns true if the item is not present, false otherwise.
bool remove(int val) Removes an item val from the multiset if present. Returns true if the item is present, false otherwise. Note that if val has multiple occurrences in the multiset, we only remove one of them.
int getRandom() Returns a random element from the current multiset of elements. The probability of each element being returned is linearly related to the number of same values the multiset contains.
You must implement the functions of the class such that each function works on average O(1) time complexity.

Note: The test cases are generated such that getRandom will only be called if there is at least one item in the RandomizedCollection.
  '''
  def insert(self, val: int) -> bool:
        if val in self.d and len(self.d[val]) > 0:
            res = False
        else:
            res = True
        self.nums.append(val)
        # store element positions
        self.d[val].add(len(self.nums)-1)
        return res
        

    def remove(self, val: int) -> bool:
        if val in self.d and len(self.d[val]) > 0:
            pos = self.d[val].pop() # element to remove position            
            lpos = len(self.nums)-1 # last position
            lval = self.nums[lpos] # last val
            
            # add lval pos first .. then remove .. so when last == val .. it will take care auto
            self.d[lval].add(pos)            
            self.d[lval].remove(lpos)
            
            # swap with last
            self.nums[pos], self.nums[lpos] = self.nums[lpos], self.nums[pos]                        
            
            # remove element
            self.nums.pop()
            return True
        return False
        

    def getRandom(self) -> int:
        size = len(self.nums)
        i = int(random.random()*size)
        return self.nums[i]
