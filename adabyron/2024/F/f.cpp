#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    string d0, m0, y0, d1, m1, y1;
    while(cin >> d0 >> m0 >> y0 >> d1 >> m1 >> y1) {
        cout << y1 << endl;
        string y1C = y1, y0C = y0;
        int r = stoi(y1) - stoi(y0) + 1;
        cout << y0C << endl;
        cout << y0C[3] + y0C[2] << endl;

    }


    return 0;
}