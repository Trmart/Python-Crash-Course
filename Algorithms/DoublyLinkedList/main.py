from doubly_linked_list import DLL

def main():
    """main"""

    list = DLL()
    list.insert_at_front(5)
    list.insert_at_end(6)
    list.insert_after_node(7,5)
    list.print_list_forward()

if(__name__=='__main__'):
    main()