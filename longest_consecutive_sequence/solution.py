def solution(nums):
    '''Easy solution using sorting

    Complexity - Time: O(NlogN), Space O(1)
    Issue: Destroys input - doesn't maintain ordering
    '''

    # easy way to remove duplicates
    nums = list(set(nums))

    if not nums:
        return [] 
    
    if len(nums) == 1:
        return [nums[0], nums[0]]  
    
    nums.sort()
    
    start, max_range = 0, 1 
    result = []
    for index in range(1, len(nums)):
        if nums[index] == nums[index - 1] + 1:
            current_range = index - start + 1
            if current_range > max_range:
                max_range = current_range
                result = [nums[start], nums[index]]
        else:
            start = index
        
    return result

def solution(nums):
    '''Improve runtime by avoiding sorting 

    Build bi-directional graph
    Each edge represent continuous sequence
    
    Use BFS to iterate over all values to find max sequence

    Complexit: Time: O(N), Space: O(N)

    Each node is traversed just twice - 1-building graph, 2-iteration
    O(2N) = O(N)

    Sapce:
    Graph and and queue both will hold max of N - so O(2N) = O(N)
    '''
    nums = set(nums)

    if not nums:
        return []

    if len(nums) == 1:
        nums = list(nums)
        return [nums[0], nums[0]]

    # build graph
    graph = {}
    for num in nums:
        graph[num] = []
        if num + 1 in nums:
            graph[num].append(num + 1)
        
        if num - 1 in nums:
            graph[num].append(num - 1)

   
    # apply BFS
    visited = set()
    result = []
    max_range = 1 
    for num in graph:
        if num in visited:
            continue 
        current_min, current_max = num, num
        q = deque([num])
 
        while q:
            current = q.popleft()
            visited.add(current)
            current_min = min(current_min, current)
            current_max = max(current_max, current)
            current_range = current_max - current_min + 1
            if current_range > max_range:
                max_range = current_range 
                result = [current_min, current_max]
                
            for item in graph[current]:
                if item not in visited:
                    q.append(item)
          
    return result
    
def solution(nums):
    '''Earlier solution builds graph - however one optimization could be 
    to build graph dynamically while performing BFS 

    > Set is used to improve access time 
    "in" operation in list in O(N) - while O(1) in set 

    Time: O(N)
    Space: O(N) (however we don't build extra graph)
    > queue is still required for BFS
    '''
    nums = set(nums)
   
    if not nums:
        return []

    if len(nums) == 1:
        nums = list(nums)
        return [nums[0], nums[0]]

    visited = set()
    result = []
    max_range = 1 
    for num in (nums - visited):
        current_min, current_max = num, num
        q = deque([num])
        
        while q:
            current = q.popleft()
            visited.add(current)
            current_min = min(current_min, current)
            current_max = max(current_max, current)
            current_range = current_max - current_min + 1
            if current_range > max_range:
                max_range = current_range 
                result = [current_min, current_max]
                
            for item in [current + 1, current - 1]:
                # nums as set ensures O(1) instead of O(N) 
                if item in nums and item not in visited:
                    q.append(item)
          
    return result
    
def solution(nums):
    '''Earlier solution doesn't maintain ordering 

    In this solution I am using a dict to hold index data that can be returned as well

    Time: O(N), Space: O(N)
    '''
    
    # compress input to hold in dict
    compressed = defaultdict(list)
    for index, num in enumerate(nums):
        compressed[num].append(index)
   
    # guard condition - for early exit
    if not compressed:
        return {}, []

    if len(compressed) == 1:
        return compressed, [nums[0], nums[0]]
   
    # bfs - building dynamic graph
    visited = set()
    result = []
    max_range = 1 
    for num in compressed:
        if num in visited:
            continue
            
        current_min, current_max = num, num
        q = deque([num])
        
        while q:
            current = q.popleft()
            visited.add(current)
            current_min = min(current_min, current)
            current_max = max(current_max, current)
            current_range = current_max - current_min + 1
            if current_range > max_range:
                max_range = current_range 
                result = [current_min, current_max]
                
            for item in [current + 1, current - 1]:
                if item in compressed and item not in visited:
                    q.append(item)
          
    return compressed, result
