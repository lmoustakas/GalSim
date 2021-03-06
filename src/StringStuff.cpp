#include "StringStuff.h"
#include <cctype>
#include <ctime>

namespace galsim {

    bool isComment(const std::string& instr) 
    {
        std::istringstream is(instr);
        std::string word1;
        is >> word1;
        return (!is || word1.empty() || word1[0]=='#');
    }

    std::istream& getlineNoComment(std::istream& is, std::string& s) 
    {
        do {
            if (!getline(is,s)) return is;
        } while (isComment(s));
        return is;
    }

    bool nocaseEqual(char c1, char c2) 
    {
        return std::toupper(c1)==std::toupper(c2);
    }

    bool nocaseEqual(const std::string& s1, const std::string& s2) 
    {
        if (s1.size() != s2.size()) return false;
        std::string::const_iterator p1=s1.begin();
        std::string::const_iterator p2=s2.begin();
        for ( ; p1!=s1.end(); ++p1, ++p2)
            if (!nocaseEqual(*p1, *p2)) return false;
        return true;
    }

    void stripTrailingBlanks(std::string& s) 
    {
        std::string::iterator tail;
        while (!s.empty()) {
            tail=s.end()-1;
            if (!std::isspace(*tail)) return;
            s.erase(tail);
        }
    }

    void stripExtension(std::string& s) 
    {
        size_t dot=s.find_last_of(".");
        if (dot==std::string::npos) return; // No extension
        s.erase(dot);
    }

    std::string taggedCommandLine(int argc, char *argv[]) 
    {
        time_t now;
        time(&now);
        std::string output = ctime(&now);
        // get rid of last character, which is linefeed:
        output.erase(output.size()-1);  // ????
        output += ": ";
        for (int i=0; i<argc; i++) {
            output += " "; output += argv[i];
        }
        return output;
    }

}
