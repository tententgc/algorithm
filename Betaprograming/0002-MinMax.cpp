#include <iostream>
using namespace std;
int main()
{
    int value, n, i, min = 2000000001, max = -2000000001;
    cin >> n;
    for (i = 0; i < n; i++)
    {
        cin >> value;
        if (value > max)
            max = value;
        if (value < min)
            min = value;
    }
    cout << min << "\n"
         << max;
    return 0;
}
