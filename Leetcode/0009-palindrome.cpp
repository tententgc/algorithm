class Solution
{
public:
    int getReverse(long int nums)
    {
        long int ans = 0;
        while (nums > 0)
        {
            long int rem = nums % 10;
            ans = (ans * 10) + rem;
            nums = nums / 10;
        }
        return ans;
    }
    bool isPalindrome(int x)
    {
        long int reverse_num = getReverse(x);
        if (x == reverse_num)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
};