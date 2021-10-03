def has_cycle(head):
    
    visted = set()
    
    while (head != None):
        if(head in visted): return 1
        visted.add(head)
        head = head.next
    
    return 0
    
