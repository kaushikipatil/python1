"""
Where is Voyager 1?
The Voyager 1 spacecraft, launched September 15, 1977, is the farthest traveling
earthmade object. It is presently on the outer edges of our solar system.
The NASA update page on September 25, 2009, reported it as being a distance of
approximately
16,637,000,000 miles from the Sun, traveling away from the Sun at 38,241 miles/hour.

Write a program that will prompt the user for an integer number that indicates the
number of days after 9/25/09. You will calculate the distance of Voyager from the Sun
using the numbers from 9/25/09 (assume that velocity is constant) plus the entered
number of days and report:
 Distance in miles
 Distance in kilometers (1.609344 kilometers/mile)
 Distance in Astronomical Units (AU, 92,955,887.6 miles/AU)
 Round trip time for radio communication in hours. Radio waves travel at the speed
of light, listed at 299,792,458 meters/second.
"""
print("Welcome to the Voyager 1 spacecraft program")

print("On September 25, 2009 it was reported it as being a distance of approximately 16,637,000,000 miles from the Sun")

print("Please inter the number of days that indicate the numbers from September 25, 2009")
no=(input())
n=int(no)
print("Okay. I see who have entered ", n," days.")

mile=(n*24*38241)
miles=(mile+16637000000)
print("Distance in miles ", miles)

kilometer=(miles * 1.609344)
print("Distance in kilometers ", kilometer)

astro= miles/92955887.6
print("Distance in Astronomical Units ", astro)

light=299792458*60*60
radio=miles/light
print("Round trip time for radio communication in hours ", radio)
