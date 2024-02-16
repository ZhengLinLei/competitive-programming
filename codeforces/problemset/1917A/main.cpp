#include <iostream>
#include <vector>
using namespace std;

int main() {
    int t;
    cin >> t;

    for (int _ = 0; _ < t; ++_) {
        int n;
        cin >> n;
        vector<int> nums(n);
        int zeros = 0, negatives = 0;
        for (int i = 0; i < n; ++i) {
            cin >> nums[i];
            if (nums[i] == 0) zeros++;
            if (nums[i] < 0) negatives++;
        }

        if (zeros == 0 && negatives % 2 == 0) {
            cout << "1\n1 0\n";
        } else {
            cout << "0\n";
        }
    }

    return 0;
}
