# Problem 12
# The Network Common-Interest Finder
# 
# You want to find shared interests between two tech founders. Represent Founder A's skills and Founder B's skills as two separate lists, convert them to an appropriate data structure, and extract a collection of only the skills they both share.


founder_a = ["Python", "JavaScript", "AWS", "Machine Learning", "Blockchain", "React"]
founder_b = ["Python", "React", "PostgreSQL", "Blockchain", "Cybersecurity", "Docker"]

fa = set(founder_a)
fb = set(founder_b)

common = fa.intersection(fb)
print(common)

