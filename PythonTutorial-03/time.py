import time

ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)
print("")

localtime = time.localtime(time.time())
print("Local current time :", localtime)
print("")

localtime = time.asctime(time.localtime(time.time()))
print("Local current time :", localtime)
print("")