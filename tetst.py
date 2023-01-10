from random import randint
class ListNode:


    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def print(self,curr_node=None):
        if curr_node is None:
            curr_node = self.head
        while curr_node is not None:
            print(curr_node.val,end=" ")
            curr_node = curr_node.next
        print()

    def reverse1(self,sentinel):
        p = sentinel.next
        while p.next is not None:
            t = p.next
            p.next = t.next
            t.next = sentinel.next
            sentinel.next = t
        #print("i just reversed")
        return (sentinel)

    def reverse(self,sentinel, k):
        p = sentinel.next
        for i in range(k - 1):
            t = p.next
            p.next = t.next
            t.next = sentinel.next
            sentinel.next = t
        #print("i just reversed")
        return (sentinel)

    def reverseKGroup(self, sentinel, k):


        # sentinel = ListNode(0, head)
        new_head = sentinel.next
        curr_head = sentinel
        i = 0
        while curr_head is not None:
            if curr_head.next is None:
                break
            curr_head = curr_head.next
            i += 1
            if i % k == 0:
                #print(curr_head.val, i)
                if i // k == 1:
                    new_head = curr_head
                curr_head = sentinel.next
                self.reverse(sentinel, k)
                sentinel = curr_head
                #self.print(new_head)

        return new_head



    def reverse_funky(self):
        sentinel = ListNode(0,self.head)
        i = 0
        k = 1
        curr_head = sentinel
        while curr_head is not None:
            if curr_head.next is None:
                break
            i+=1
            curr_head = curr_head.next
            print(i,k)
            if i%k == 0:
                if k%2==0:
                    curr_head = sentinel.next
                    self.reverse(sentinel, k)
                sentinel=curr_head
                k += 1
                i=0
        if i % 2 == 0:
            self.reverse(sentinel, i)

    def __init__(self,l : list):
        sentinel = ListNode(0,None)
        c = sentinel
        for i in l:
            temp = ListNode(i,None)
            c.next = temp
            c = c.next
        self.head = sentinel.next


    def __init1__(self,k:int,l:int):
        self.head = ListNode(k)
        curr_node = self.head
        for i in range(k+1,l+1):
            #temp = ListNode(randint(1,20))
            temp = ListNode(k)
            curr_node.next = temp
            curr_node = temp


    def removeNthFromEnd(self, head , n: int) :

        sz = 0
        node = head
        while node is not None:
            node = node.next
            sz += 1
        print(sz)
        index = 1
        node = head
        while node is not None:
            node = head.next
            index += 1
            if index == sz - n:
                node.next = node.next.next
                break

    def reverseBetween1(self, head, left: int, right: int) :
        if head is None:
            return head
        sentinel = ListNode(0, head)
        p = sentinel.next
        reverse = False
        while p.next is not None:
            if p.next.val == left:
                reverse = True
                s=p
                p=p.next
            if reverse:
                t = p.next
                p.next = t.next
                t.next = s.next
                s.next = t
                if s.next.val == right:
                    reverse = False
            else:
                p=p.next
        return (sentinel.next)

    def mergesortedlist(self,list1,list2):
        if list1 == None:
            if list2 == None:
                return None
            else:
                return list2
        elif list2 == None:
            if list1 == None:
                return None
            else:
                return list1
        a = list1
        b = list2
        sentinel = ListNode(0, None)
        c = sentinel
        while a is not None and b is not None:
            if a.val > b.val:
                c.next = b
                b = b.next
            else:
                c.next = a
                a = a.next
            c = c.next
            if a is None:
                c.next = b
            elif b is None:
                c.next = a

        return sentinel.next

    def reverseBetween(self, head, left, right) :
        if left == right:
            return head
        sentinel = ListNode(0, head)
        p = sentinel
        reverse = False
        index = 0
        while p.next is not None:
            if index == left - 1:
                reverse = True
                s = p
                p = p.next
            if reverse:
                t = p.next
                p.next = t.next
                t.next = s.next
                s.next = t
                if index == right - 2:
                    reverse = False
            else:
                p = p.next
            index += 1
        return (sentinel.next)

    def maxtwinns(self):
        sentinel = ListNode(0,self.head)
        mid = sentinel
        curr_node = sentinel
        index =0
        while curr_node.next is not None:
            curr_node=curr_node.next
            index+=1
            if index%2==0:
                mid = mid.next
        print(mid.val)
        self.reverse1(mid)
        max = -1
        curr_node = sentinel.next
        curr_node_mid = mid.next
        while curr_node is not mid.next:
            sum = curr_node.val + curr_node_mid.val
            if sum > max:
                max = sum
            curr_node=curr_node.next
            curr_node_mid = curr_node_mid.next
        return max


    def mergeKLists(self,lists):
        if lists is None:
            return None
        sentinel = ListNode(0, None)
        c = sentinel
        #lists.remove(None)
        while len(lists) != 0:
            min_val,min_pointer,min_index = min([(x.val,x,i) for i,x in enumerate(lists)],key=lambda x:x[0])
            print(min_pointer.val, min_index)
            #for i in range(len(lists)):
            #    if lists[i].val < min_pointer.val:
            #        min_pointer = l
            #        min_index = i
            #print(min_pointer.val,min_index)
            c.next = min_pointer
            lists[min_index]  = min_pointer.next
            c = c.next
            if None in lists:
                lists.remove(None)
            print([x.val for x in lists])

        return sentinel.next

    def mergeKLists1(self,lists):
        if lists is None:
            return None
        l = len(lists)
        for i in range(l):
            if lists[i] is not None:
                break
        sentinel = ListNode(0, lists[i])

        #lists.remove(None)
        for i in range(i+1,l):
            if lists[i] is None:
                continue
            else:
                b = lists[i]
                a=sentinel
                self.print(a)
                while b is not None:
                    if a.next.val > b.val:
                        temp = b.next
                        b.next = a.next
                        a.next =b
                        a=a.next
                        b=temp
                    else:
                        a=a.next
                    if a.next is None:
                        a.next = b
                        break




        return sentinel.next



s = Solution([1,3,5,6])
#s = Solution([])
#s.print()
s1 = Solution([2,4,6,7])
#s1 = Solution([])
#s1.print()

s2 = Solution([3,5,8,9])
#s2 = Solution([])
#s2.print()
#s.print()
#sentinel = ListNode(0, s.head)
#s.print(s.reverseKGroup(sentinel,2))
#s.print(s.reverse(s.head.next,2))
#s.reverse_funky()
#s.reverseBetween(s.head,4,11)
#s.maxtwinns()
#s.print()
#s.removeNthFromEnd(s.head,2)
l = [s.head,s1.head,s2.head]
for i in l:
    s.print(i)
s.print(s.mergeKLists1(l))


