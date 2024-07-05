'''' '''

def generate_groups (team,*args):
    print(team,':')
    for i in args: ## loops through the args
        print(i)
print(generate_groups('Team-1','Test','Brook','David','IT')) #first arg defaulted to the first param team.
## the rest are args of the param *args