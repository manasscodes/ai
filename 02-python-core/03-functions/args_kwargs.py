# Demonstrating *args and **kwargs
def display_args(*args):
    for arg in args:
        print("Arg:", arg)

def display_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

display_args(1, 2, 3, "AI")
display_kwargs(name="Manas", role="Engineer", track="AI")