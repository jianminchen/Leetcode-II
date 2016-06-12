#include <climits>

class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        vector <int> index (primes.size());
        vector <int> super_ugly;
        super_ugly.push_back(1);
        
        while (super_ugly.size()<n)
        {
            long long int minn=INT_MAX;
            int min_ind=0;
            for(int i=0;i<primes.size();i++)
            {
                if(primes[i]*super_ugly[index[i]]<minn)
                {
                    minn=primes[i]*super_ugly[index[i]];
                    min_ind=i;
                }
            }
            if(minn!=super_ugly[super_ugly.size()-1])
                super_ugly.push_back(minn);
            index[min_ind]++;
        }
        return super_ugly[n-1];
    }
};
