#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'marsExploration' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts STRING s as parameter.
 */

int marsExploration(string s) {
    int ret=0;
    for (int i=0;i<s.size(); i++) {
        if(i%3==1 ) {
            if (s[i]!='O') {
                ret++;
            }
        } else {
            if (s[i]!='S') {
                ret++;
            }
        }
    }
    return ret;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    int result = marsExploration(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
