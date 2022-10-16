class Solution
{
public:
    int searchInsert(vector<int> &v, int t)
    {
        int pos = lower_bound(v.begin(), v.end(), t) - v.begin();
        return pos;
    }
};