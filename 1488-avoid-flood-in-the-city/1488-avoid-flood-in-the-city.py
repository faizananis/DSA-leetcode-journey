class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        last_filled = {}      # stores: lake -> last day it was filled
        dry_days = []         # stores all indices where rains[day] == 0
        ans = [1] * n         # default for all dry days

        for day in range(n):
            lake = rains[day]

            if lake == 0:
                # record this dry day for later use
                dry_days.append(day)
            else:
                ans[day] = -1  # raining day — can't dry any lake

                if lake in last_filled:
                    # this lake already got rain before — it must be dried before today
                    last_day = last_filled[lake]

                    # find a dry day that comes AFTER that day
                    found = False
                    for d in dry_days:
                        if d > last_day:
                            ans[d] = lake     # dry this lake on that dry day
                            dry_days.remove(d)
                            found = True
                            break

                    if not found:
                        # no dry day available — flood occurs
                        return []

                # update the latest day this lake got rain
                last_filled[lake] = day

        return ans

        