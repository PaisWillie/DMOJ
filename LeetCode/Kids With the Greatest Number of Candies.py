# Problem: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        # 1. Get the highest number of candies that a kid has
        most_amount_of_candies = max(candies)

        # 2. Create a temporarily empty list []
        kids_with_greatest_amounts_of_candies = []

        # 3. Use a for loop to go through each kid/index of the list
        for i in range(len(candies)):

            # 4. Add the # of candies each kid has + # of extraCandies
            # 5. Compare the total to the most_amount_of_candies
            kids_with_greatest_amounts_of_candies.append(
                candies[i] + extraCandies >= most_amount_of_candies)

        # Return list
        return kids_with_greatest_amounts_of_candies
