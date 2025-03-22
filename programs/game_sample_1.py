# A sample of how poetry game will work.

introduction = """Complete the poem
use the answer to the riddle to fill in the gaps in the poem."""

print(f"{introduction}\n")

print("\tcaged bird!\n")

poem_1 = """A free bird leaps
on the back of the wind
and floats downstream
till the current ends
and dips his ----
in the orange sun rays"""
print(f"{poem_1}\n")

riddle_1 = """I have feathers, but I'm not a bird.
I can help you fly, but I can't fly myself.
I'm a part of a bird, but I'm not the whole thing.
What am I?"""
print(f"Riddle:\n\t{riddle_1}\n")

prompt = input("Fill the gaps in the poem using the riddle above: , Your answer is a 5 letter word.")
active = True

while active:
    if prompt == "wings":
        print("Nice one!")
        active = False
    else:
        print("Try again!")
        break
