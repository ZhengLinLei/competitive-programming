#include <bits/stdc++.h>

using namespace std;

int main() {
    int t; cin >> t;
    for (int i = 0; i < t; i++) {
        long long k, s, n; cin >> k >> s >> n;
        if (n - (k*s) < 0) {
            cout << "Imposible" << endl;
        }
        else {
            if (n % 2 !=0) {
                if (k % 2 == 0) {
                    n = n - (k+1);
                    s--;
                }
                else {
                    n = n-k;
                    s--;
                }
                if (s == 0 && n != 0) cout << "Imposible" << endl; continue;
                n = n - (k*s);
                if (n >= 0 && n % 2 == 0) {
                    cout << "Posible" << endl;
                }
                else cout << "Imposible" << endl;
            }
            else {
                if (k % 2 != 0) {
                    n = n -(k+1);
                    s--;
                }
                else {
                    n = n-k;
                    s--;
                }
                if (s == 0 && n != 0) cout << "Imposible" << endl; continue;
                if (n >= 0 && n & 2 == 0) {
                    cout << "Posible" << endl;
                }
                else cout << "Imposible" << endl;
            }
        }
    }
    return 0;
}