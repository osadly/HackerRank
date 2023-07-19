#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

string timeInWords(int h, int m) {
vector<string> minAsTxt = {"","one minute","two minutes","three minutes","four minutes","five minutes","six minutes","seven minutes","eight minutes","nine minutes","ten minutes","eleven minutes","twelve minutes","thirteen minutes","fourteen minutes","quarter","sixteen minutes","seventeen minutes","eighteen minutes","nineteen minutes","twenty minutes","twenty one minutes","twenty two minutes","twenty three minutes","twenty four minutes","twenty five minutes","twenty six minutes","twenty seven minutes","twenty eight minutes","twenty nine minutes","half"};
    
    vector<string> hrAsTxt = {"","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve"};
    string ret="";
    /*if(m==1) {
        ret+="one minute past ";
    } else if (m==15) { 
        ret+="quarter past ";
    } else if (m==30) { 
        ret+="half past ";
    } else */
    if (m==0) {
        return hrAsTxt[h]+" o\' clock";
    }
    else if (m>0 && m<=30) {
        return minAsTxt[m] + " past " + hrAsTxt[h];
    } else if (m>30 && m<60) {
        if(h<12) {
            return minAsTxt[60-m] + " to " + hrAsTxt[h+1];
        } else {
            return minAsTxt[60-m] + " to one";
        }
    }
    
    return ret;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string h_temp;
    getline(cin, h_temp);

    int h = stoi(ltrim(rtrim(h_temp)));

    string m_temp;
    getline(cin, m_temp);

    int m = stoi(ltrim(rtrim(m_temp)));

    string result = timeInWords(h, m);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
