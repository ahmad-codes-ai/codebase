# Problem 27
# The Beta Tester Invitation Filter
# 
# You want to invite distinct users to a Discord server. You have a list of email addresses from Launch Day and another list from Day 2. Use a set operation to compile a single collection of unique emails that handles users who signed up on both days.


launch_day = ["alice@example.com", "bob@example.com", "charlie@example.com", "diana@example.com", "eve@example.com"]

day_two = ["charlie@example.com", "frank@example.com", "grace@example.com", "alice@example.com", "henry@example.com"]

ld = set(launch_day)
dt = set(day_two)

invite = list(ld.union(dt))
print(invite)

