'''
Implement a depth-first traversal iteratively
'''

def iter_dft(root):
    '''
    Visits the nodes of the tree in depth-first order
    returns a list of the visited values
    
    Order but without recursion

    Since we noticed that traversing using recursion visits the nodes of the tree in LIFO ordering, we can use a stack to achieve the same effect
    '''

    stack = []
    result = []

    # what do we initially add to our stack?
    # add our initial root node to our stack
    stack.append(root)

    # how do we loop through our tree?
    # add and remove nodes from our stack
    while len(stack) > 0:
        #pop off the top stack element
        #this is the current node we're visiting
        current = stack.pop()

        #add the current nodes children to the stack (if it has children)
        if current.left is not None:
            stack.append(current.left)

        if current.right is not None:
            stack.append(current.right)

        result.append(current.value)

    return result



from collections import deque

def breadthFirstTraversal(root):
    #visits the nodes of the tree in a bft order
    #adds all the nodes to a result list and returns it
    
    queue = deque() # holds on to nodes
    result = [] #holds on to value

    queue.append(root)

    while len(queue) > 0:
        #dequeue the node that was added earliest to the queue
        current = queue.popleft()
        result.append(current.value)

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)

    return result

