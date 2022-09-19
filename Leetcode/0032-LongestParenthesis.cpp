class Solution
{
public:
    int longestValidParentheses(string s)
    {
        int n = s.size();
        int ans = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                if (s[i] == '(' && s[j] == ')')
                {
                    int cnt = 0;
                    for (int k = i; k <= j; k++)
                    {
                        if (s[k] == '(')
                            cnt++;
                        else
                            cnt--;
                        if (cnt < 0)
                            break;
                    }
                    if (cnt == 0)
                        ans = max(ans, j - i + 1);
                }
            }
        }
        return ans;
    }
};