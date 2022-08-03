from bisect import bisect_left

class MyCalendar:
    def __init__(self):
        self.booked = [(-1,0)]

    def book(self, start: int, end: int) -> bool:
        #for i in range(len(self.booked)):
        i = bisect_left(self.booked, (start,end)) - 1
        event = self.booked[i]
        if event[1] <= start:
            if i + 1 < len(self.booked):
                if end <= self.booked[i+1][0]:
                    self.booked.insert(i+1, (start, end))
                    return True
            else:
                self.booked.insert(i+1, (start, end))
                return True
        return False
                

myCalendar = MyCalendar()
a = myCalendar.book(10, 20); # return True
print(a)
a = myCalendar.book(15, 25); # return False, It can not be booked because time 15 is already booked by another event.
print(a)
a = myCalendar.book(20, 30); # return True, The event can be booked, 
print(a)