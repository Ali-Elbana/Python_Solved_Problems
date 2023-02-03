import os

os.system('cls')

print()
# Write your code here:
 
 
timer_resolution = int( input( "Please enter the timer resolution: " ) )

system_freq = float( input( "Please enter the system frequency in MHZ: " ) )

prescaler_value = int( input( "Please enter the prescaler value: " ) )

timer_ovf = float( (2 ** timer_resolution) *  ( (prescaler_value / system_freq) * (10 ** -3) ) ) 

print( f'The timer will overflow after {timer_ovf} ms' )


# The end of your code. 
print(), print()
