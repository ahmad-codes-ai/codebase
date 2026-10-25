from helpers import *



user = input("Enter the org you want repos for: ")

s = fetch_org(user)
sort_repos()
print(f'Total repos fetched: {len(s)}')

m = get_sorted_repo(10)
print('Top 10 repos')
print()


for i in m:
    print(i)
    print()
