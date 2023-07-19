#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'makingAnagrams' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. STRING s1
 *  2. STRING s2
 */

int makingAnagrams(string s1, string s2) {
    int x=int('a');
    int n1=0,n2=0,ret=0;
    for (int i=0; i<26; i++) {
        n1=std::count(s1.begin(),s1.end(),x+i);
        n2=std::count(s2.begin(),s2.end(),x+i);
        ret+=abs(n1-n2);
    }
    return ret;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s1;
    getline(cin, s1);

    string s2;
    getline(cin, s2);

    int result = makingAnagrams(s1, s2);

    fout << result << "\n";

    fout.close();

    return 0;
}
