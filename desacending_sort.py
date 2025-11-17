def insert_in_sorted_order(stack, element):
    if not stack or element >= stack[-1]:
        stack.append(element)
        return
    
    temp = stack.pop()
    insert_in_sorted_order(stack, element)
    stack.append(temp)

def sort_stack(stack):
    if not stack:
        return
    
    temp = stack.pop()
    sort_stack(stack)
    insert_in_sorted_order(stack, temp)
