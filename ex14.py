from sys import argv

script, username = argv

prompt = '> '

print(f" Hi {username}, I'm the {script}")
print(f' do you like my {username}')
like = input(prompt)
 
print(f" where do you live {username}")
live = input(prompt)

print(f"what kind of computer do you have {username}")
computer = input(prompt)

print(f"""
Alright, so you said {like} about liking me.
You live in {live}.  Not sure where that is.
And you have a {computer} computer.  Nice.
""")