class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        
        for i in range(1, num + 1):
            digit_sum = 0
            n = i
            
            # Digit sum calculate chey
            while n > 0:
                digit_sum += n % 10  # Last digit teesko
                n //= 10             # Last digit teesi veyyi
            
            # Even unda check chey
            if digit_sum % 2 == 0:
                count += 1
                
        return count 