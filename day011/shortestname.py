def find_shortest_name(names):
    short_len = 100
    shortest = ""

    for name in names:
        if len(name) < short_len:
            short_len = len(name)
            shortest = name
    
    return shortest

names = ['subanghi', 'arun', 'santhosh']
answer = find_shortest_name(names)
print(f'shortest among {names} is {answer}!')
