class Solution
{
public:
    string countAndSay(int n)
    {

        // Base Case 1
        if (n == 1)
        {
            return "1";
        }

        // Base Case 2
        if (n == 2)
        {
            return "11";
        }

        string str = "11";
        for (int i = 3; i <= n; i++)
        {
            // Adding extra char fro a break condition
            str += "$";
            string temp = "";
            int count = 1;
            for (int j = 1; j < str.length(); j++)
            {
                // When we don't find duplicates that means we will add the count and last non-repeating character to 'temp' and make count = 1
                if (str[j] != str[j - 1])
                {
                    temp += to_string(count);
                    temp += str[j - 1];
                    count = 1;
                }
                // When we find duplicates, then we increase the frequency of that element
                else
                {
                    count++;
                }
            }
            // Updating str with the new temp to get the next valid answer
            str = temp;
        }
        return str;
    }
};