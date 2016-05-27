class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n=nums.size();
        if (n==0)
            return 0;
        vector<int> T(n+1);
        T[1]=1;
        int maxx=1;
        for(int i=2; i<n+1; i++)
        {
            int temp=1;
            for(int j=1; j<i; j++)
            {
                if(nums[j-1]<nums[i-1])
                    temp=max(temp,T[j]+1);
            }
            T[i]=temp;
            maxx=max(maxx,T[i]);
        }
        return maxx;
    }
};
