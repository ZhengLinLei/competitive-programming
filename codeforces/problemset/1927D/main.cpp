#include <iostream>
#include <vector>
using namespace std;

void printF(int x, int y) {
    cout << x << " " << y << endl;
}

int main() {
    int t;
    cin >> t;
    
    for (int _ = 0; _ < t; ++_) {
        int n;
        cin >> n;
        vector<int> arr(n);
        for (int i = 0; i < n; ++i) {
            cin >> arr[i];
        }
        
        int q;
        cin >> q;
        for (int _ = 0; _ < q; ++_) {
            int i, j;
            cin >> i >> j;
            i--; j--; // adjust to 0-based indexing
            
            int tmp = i + 1;
            bool cut = false;
            while (i < j) {
                while (tmp <= j) {
                    if (arr[i] != arr[tmp]) {
                        printF(i+1, tmp+1);
                        cut = true;
                        break;
                    }
                    tmp++;
                }
                if (cut) break;
                i++;
            }
            if (cut) continue;
            printF(-1, -1);
        }
        cout << endl;
    }
    
    return 0;
}
