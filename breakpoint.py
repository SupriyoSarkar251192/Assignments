# 19. Create a python program that demonstrates setting a breakpoint() and inspecting variables using the debugger.
"""
Use modes in Pdb:
n - next line
c - continue till next breakpoint
q - quit Pdb console
s - execute the current line and stop at the first possible opportunity
"""
for i in range(4):
    breakpoint()
    print(i)
