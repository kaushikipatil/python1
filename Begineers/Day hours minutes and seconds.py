"""
A day has 86,400 secs (24*60*60). Given a number in the range 1–86,400, output the
current time as hours, minutes, and seconds with a 24-hour clock. For example, 70,000
sec is 19 hours, 26 minutes, and 40 seconds
"""

print("Enter the number in seconds in between 1-86400")
n=int(input())

hours=float(n/60/60)
hr=int(hours)

minutes=float((hours-hr)*60)
min=int(minutes)

seconds=int((minutes-min)*60)

print(n," seconds will be ",hr," hour, ",min," minutes, and ",seconds," seconds.")
