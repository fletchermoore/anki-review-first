Review First
============

This is a very simple addon which simply reorders the way Anki retrieves the next card. This is for the traditional scheduler.
No changes are made to the experimental scheduler, mainly because I don't use it because I heavily rely on AnkiAndroid.

Anki has 3 queues of cards: new, learning, and review. The new cards have not yet been seen (blue number). The learning cards
are shown frequently with multiple steps before they are considered learned (red number). The cards which have been learned
and are now due for review are the final queue (green number).

By default, Anki will show the learning cards first, then due review cards or new cards based on user preference. I find this problematic,
as once I have accumulated a lot of cards which are due, it is hard to get through them all in a short amount of time
when the learning cards keep getting shown. This addon addresses this problem by reordering the queues. If this addon is enabled
review cards will be shown first until there are none left. Then
learning and new cards will be shown as normal.