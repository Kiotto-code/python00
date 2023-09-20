import time as t
import datetime as dt

# time.time() function returns the current time in seconds since the "epoch." 
# The "epoch" is a reference point in time, and in most systems, it is set to 
# January 1, 1970 (UTC).
current_time_seconds = t.time()

scientific_notation = "{:.2e}".format(current_time_seconds)

# strftime("%b %d %Y") formats the current date and time as a string.
# %b represents the abbreviated month name (e.g., "Sep" for September).
# %d represents the day of the month with leading zeros.
# %Y represents the four-digit year.
current_date = dt.datetime.now().strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {current_time_seconds:,.4f} \
or {scientific_notation} in scientific notation")
print(current_date)
