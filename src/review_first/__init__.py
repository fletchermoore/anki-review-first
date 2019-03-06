
import anki.sched as Sched

# ORIGINAL FUNCTION
    # def _getCard(self):
    #     "Return the next due card id, or None."
    #     # learning card due?
    #     c = self._getLrnCard()
    #     if c:
    #         return c
    #     # new first, or time for one?
    #     if self._timeForNewCard():
    #         c = self._getNewCard()
    #         if c:
    #             return c
    #     # card due for review?
    #     c = self._getRevCard()
    #     if c:
    #         return c
    #     # day learning card due?
    #     c = self._getLrnDayCard()
    #     if c:
    #         return c
    #     # new cards left?
    #     c = self._getNewCard()
    #     if c:
    #         return c
    #     # collapse or finish
    #     return self._getLrnCard(collapse=True)


def reorderedGetCard(self):
        "Return the next due card id, or None."
        # if you review first, there is no initial filling of the learn queue
        # once you miss a card, it gets added to the learn queue
        # this causes the program to think the learn queue consists of only your misses
        # to avoid this, we will fill the learn queue right now
        self._fillLrn()

        # card due for review?
        # this call has been moved to first from below
        c = self._getRevCard()
        if c:
            return c

        # the remainder of this function is the same as it was previously.
        # learning card due?
        c = self._getLrnCard()
        if c:
            return c
        # new first, or time for one?
        if self._timeForNewCard():
            c = self._getNewCard()
            if c:
                return c
        # day learning card due?
        c = self._getLrnDayCard()
        if c:
            return c
        # new cards left?
        c = self._getNewCard()
        if c:
            return c
        # collapse or finish
        return self._getLrnCard(collapse=True)



Sched.Scheduler._getCard = reorderedGetCard
