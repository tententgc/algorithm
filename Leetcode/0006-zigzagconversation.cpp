class Solution {
public:
    string convert(string s, int numRows) {
        int n = s.size(), wavelength = (numRows-1) << 1; 
        if(n <= numRows || numRows == 1) return s;
        string ans = "";
        for(int i = 0; i < numRows; i++){
            if(i == 0 || i == numRows - 1){
                int idx = i;
                while(idx < n){
                    ans += s[idx];
                    idx+=wavelength;
                }
            }else{
                int diff = wavelength-(i<<1);
                int idx = i;
                while(idx < n){
                    ans+=s[idx];
                    idx += diff;
                    diff = wavelength-diff;
                }
            }
        }
        return ans;
    }
};