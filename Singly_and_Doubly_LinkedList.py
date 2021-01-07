'''
Doubly_Linked_list
'''
'''
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Dll:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, data):
        if (self.head == None):
            node = Node(data)
            self.head = node
        else:
            node = Node(data, self.head)
            self.head = node
            self.head.next.prev = self.head

    def display(self, dir=None):
        if(dir == 'f'):
            strr = " "
            itr = self.head
            while(itr):
                strr = strr + str(itr.data) + "-->"
                itr = itr.next
            print(strr)

        if(dir == 'b'):
            strr = " "
            itr = self.head
            while(itr.next):
                itr = itr.next

            while(True):
                strr = strr + str(itr.data) + "-->"
                if(itr.prev):
                    itr = itr.prev
                else:
                    break
                # print(itr.data)
            print(strr)

    def length(self):
        counter = 0
        while(self.head):
            counter = counter + 1
            self.head = self.head.next
        print(counter)


dl = Dll()
dl.insert_at_beg(45)
dl.insert_at_beg(50)
dl.insert_at_beg(60)
dl.insert_at_beg(600)
dl.display("f")
dl.display("b")
dl.length()
'''


'''
Singly_Linked_list
'''
    '''
   class Node:
       def __init__(self, data, next=None):
           self.data = data
           self.next = next


   class Linkedlist:
       def __init__(self):
           self.head = None
           #self.tail = None

       def insert_at_beg(self, data):
           node = Node(data, self.head)
           self.head = node

       def Disp_list(self):
           if (self.head is None):
               return print("List is Empty!")

           listt = " "
           curr = self.head
           while(curr):
               listt = listt + str(curr.data) + "-->"
               curr = curr.next
           ll = "Linked list is:{}".format(listt)
           print(ll)

       def insert_at_end(self, data):
           if(not self.head):
               node = Node(data)
               self.head = node
           else:
               node = Node(data)
               curr = self.head
               while(curr.next):
                   curr = curr.next
               curr.next = node

       def insert_value(self, values):
           for i in range(len(values)):
               self.insert_at_end(values[i])

       def insert_aft_val(self, val, vall):
           itr = self.head
           while(itr):
               if itr.data == val:
                   node = Node(vall, itr.next)
                   node.next = itr.next
                   itr.next = node

               itr = itr.next


   l = Linkedlist()
   l.insert_at_end(58)
   l.insert_value(["banana", "mango", "grapes", "orange"])
   l.insert_aft_val("mango", "pineapple")
   l.insert_aft_val("pineapple", "strawberry")
   l.Disp_list()
   '''
