"""You are implementing a program to use as your calendar. We can add a new event 
if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection
(i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that
represents a booking on the half-open interval [start, end), the range of real 
numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added 
to the calendar successfully without causing a double booking. Otherwise, 
return false and do not add the event to the calendar.
 

Example 1:

Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, 
It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True,
The event can be booked, as the first event takes every
time less than 20, but not including 20."""


class MyCalendar:
    def __init__(self):
        self.cal = []

    def book(self, start: int, end: int) -> bool:
        for i in self.cal:
            s, e = i[0], i[1]
            if start < e and end > s:
                return False
        self.cal.append([start, end])
        return True


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
start, end = 10, 20
param_1 = obj.book(start, end)
print(param_1)
start, end = 15, 25
param_1 = obj.book(start, end)
print(param_1)
start, end = 20, 30
param_1 = obj.book(start, end)
print(param_1)
