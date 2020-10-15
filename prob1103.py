class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        x = 1
        while True:
            if sum([((x*(x-1))//2) * num_people + i * x for i in range(1, num_people+1)]) > candies:
                x -= 1
                break
            x += 1
        ans = [((x*(x-1))//2) * num_people + i * x for i in range(1, num_people+1)]
        rest = candies - sum(ans)
        i = 1
        while rest > 0:
            candy = x * num_people + i
            candy = candy if rest >= candy else rest
            ans[i-1] += candy
            rest -= candy
            i += 1
        return ans
        """
x = 1          1  2  3  4  5
x = 2     n+1  6  7  8  9 10
x = 3    2n+1 11 12 13 14 15
x = 4         16 17 18 19 20
        ------------------------
         sum: 34 38 42 46 50
           i:  1  2  3  4  5
        sum[i] = ((x*(x-1))//2) * n + i * x
        
        """
