# Assignment: Call Center--You're creating a program for a call center. Every time a call comes in you need a way to track that call. One of your program's requirements is to store calls in a queue while callers wait to speak with a call center employee. Create two classes:

# Call Class
from datetime import datetime
import itertools

class Call(object):
    # Attributes: unique id, caller name, caller phone number, time of call, reason for call
    newid = itertools.count().next
    def __init__( self, caller_name, caller_phone, call_reason ):
        self.id = Call.newid()
        self.caller_name = caller_name
        self.caller_phone = caller_phone 
        self.call_time = datetime.now()
        self.call_reason = call_reason
# Methods:
# 1) display: that prints all Call attributes.
    def displayCallInfo(self):
        print "--- Call Info ---"
        print "  ID:", self.id
        print "  Caller Name:", self.caller_name
        print "  Caller Phone:", str(self.caller_phone)[0:3]+"-"+str(self.caller_phone)[3:6]+"-"+str(self.caller_phone)[5:9]
        print "  Time of Call:", self.call_time
        print "  Reason for Call:", self.call_reason
        return self

# CallCenter Class
class CallCenter(object):
# Attributes: i) calls: should be a list of call objects;  ii) queue size: should be the length of the call list
    def __init__( self, calls, queue_size=0 ):
        self.calls = calls
        self.queue_size = queue_size
# Methods:
# 1) add: adds a new call to the end of the call list
    def addCall(self, name, phone, reason):
        self.calls.append(Call(name, phone, reason))
        self.queue_size+=1
        print "added call to end of queue"
        return self
# 2) remove: removes the call from the beginning of the list (index 0)
    def removeCall(self):
        self.calls.pop(0)
        self.queue_size-=1
        print "removed call from front of queue"
        return self
# 3) info: prints the name and phone number for each call in the queue as well as the length of the queue.
    def queueInfo(self):
        print "*** Queue Info ***"
        print "  Queue Length:", self.queue_size
        for i in range(self.queue_size):
            self.calls[i].displayCallInfo()
        return self
# Ninja Level: add a method to call center class that can find and remove a call from the queue according to the phone number of the caller.
    def removeCallBasedOnPhone(self, phone):
        #find call array index in queuue containing call object to be removed
        for i in range( self.queue_size ):
            indx = -1
            if self.calls[i].caller_phone == phone:
                indx = i
                break
        # if indx >= 0, then call to be removed was found in self.calls
        if indx >= 0:
            # object to be removed exists at self.calls[indx], so move everything forward by one position, starting at indx
            for i in range(indx, self.queue_size-1):
                self.calls[i] = self.calls[i+1]    
            #now remove last position in calls list
            self.calls.pop()
            # and reduce queue_size by 1
            self.queue_size-=1
            print "removed call of", phone, "from queue"
        else:
            print "Cannot remove call. Phone number does not exist in queue"
        return self

# Hacker Level: What if your calls get out of order? Add a method to the call center class that sorts the calls in the queue according to time of call in ascending order.
    def sortCallsBasedOnIdReverse(self):
        # use python sort-in-place function
        #first trying it with sorting by reverse order on id (easier than time)
        self.calls.sort(key=lambda call: call.id, reverse=True)
        print "Sorted calls in descending order based on ID"
        return self
    def sortCallsBasedOnTime(self):
        # use python sort-in-place function to sort on call_time
        self.calls.sort(key=lambda call: call.call_time)
        print "Sorted calls in ascending order based on call_time"
        return self

# ____________________TESTING______________________
# Test your code to prove that it works. 
# Test Caller class and display method
# Test CallCenter call and addCall, removeCall, and queueInfo methods

#First, must instantiate a CallCenter
calls = []
newcenter = CallCenter(calls)

#add calls to call center
CallCenter.addCall(newcenter,"Cindy Kalkomey", 2147330702, "login error")
CallCenter.addCall(newcenter,"Kurt Kalkomey", 2148348937, "data error")
CallCenter.addCall(newcenter,"Chloe Kalkomey", 2149991111, "cat error")
CallCenter.addCall(newcenter,"Maizie Kalkomey", 2148881111, "dog error")
CallCenter.addCall(newcenter,"Zoe Kalkomey", 2147771111, "zoe error")
CallCenter.addCall(newcenter,"Ann Thomas", 5176349888, "payment error")
CallCenter.addCall(newcenter,"Terry Thomas", 2037673544, "casino error")

#display queue
CallCenter.queueInfo(newcenter)
# remove a call from first position in queue and display queue
CallCenter.removeCall(newcenter).queueInfo()
# remove another call from first position in queue and display queue again -- and here's another (less concise way) to call the two call center methods removeCall and queueInfo
CallCenter.removeCall(newcenter)
CallCenter.queueInfo(newcenter)

# Test Ninja Level: remove call from queue based on phone number
CallCenter.removeCallBasedOnPhone(newcenter, 2148881111).queueInfo()

# Test Hacker Level: sort calls in queue in reverse order based on call.id
CallCenter.sortCallsBasedOnIdReverse(newcenter).queueInfo()

# Test Hacker Level: sort calls in queue in ascending order based on call.call_time
CallCenter.sortCallsBasedOnTime(newcenter).queueInfo()