<h1>Sleep Sort</h1>
<h3>Overview</h3>
Sleep sort is an inefficient but fun way of sorting data. The algorithm uses cpu threads initialized using pythons threading package in addition to python's sleep function. The threads, running side by side, sleep for the <u>duration of the magnitude</u> of every data point in a standard python list (could be any data structure with a little tweaking), and when the thread finishes sleeping it appends the data to another list.

This sorted list is then deep copied to the original list after the threads are all finished running

<h3>Efficiency</h3>
As you would expect, this sort algorithm isn't fast. An immediate thought to speed things up a bit would be to divide the data by some wisely chosen constant before sleeping, but that accentuates the many core flaws with this sort: it relies on system time. If my data is extrememly small, i cannot rely on system time to handle the threads how i want it to. Something might come up and the cpu could have to put a few of my threads aside to deal with it, skewing the sleep schedule of some of the data. This flaw (in addition to the obvious one) unfortunately makes the algorithm completely obsolete.

<h2>Time/Space Complexity</h2>
The algorithm runs in O(n(log(n)+1) + max(inputs)) time and a O(2) space complexity.
