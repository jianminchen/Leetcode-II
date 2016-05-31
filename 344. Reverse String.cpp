class Solution {
public:
    string reverseString(string s) {
        string res="";
        for(int i=0;i<s.size();i++)
            res=s[i]+res;
        return res;
    }
};
