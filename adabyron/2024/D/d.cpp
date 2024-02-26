#include <iostream>

using namespace std;

int main() {
    long long x;
    int t = 1;
    while(cin >> x) {
        long long n = x * 2;
        if (x == 1 ) {
            cout << "Caso #" << t << ": " << 0 << '\n';
        }
        else if (x == 3) {
            cout << "Caso #" << t << ": " << 8 << '\n';
        }
        else if (n % 4 == 0) {
            cout << "Caso #" << t << ": " << n * (n/4) << '\n';
        }
        else {
            cout << "Caso #" << t << ": " << ((n - 2) * ((n-2)/4)) + (n - 2) << '\n';
        }
        t++;
    }

    return 0;
}