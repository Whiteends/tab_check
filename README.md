# tab_check
This script notifies a user when there are too many browser tabs opened
It  checks if any of the popular browsers (firefox, chrome, safari, opera, edge) are present in the list. If any of these browsers are present, it then checks if the memory usage of the current process is greater than 2 GB (2000000000 bytes). If this condition is met, the script uses the subprocess library to notify the user through the system notification that there are too many browser tabs open and that some should be closed to save memory. The script runs this check every 60 seconds and can be run in the background.
