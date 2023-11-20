#include <filesystem>
#include <iostream>
#include <string>
#include <fstream>

void sort(char* prefix)
{
    //  TODO: бл€€€€ть сука ебучие массивы в си++ короче сука
    std::vector<std::string> entities;
    std::ofstream ConfigFile("cfg.sfes");
    ConfigFile << prefix;
    ConfigFile.close();
    std::cout << "This doesn't work yet, prefix is '" << prefix << "'" << std::endl;
    std::string path = "./";
    for (const auto& entry : std::filesystem::directory_iterator(path))
    {
        entities.push_back(entry.path().u8string());
        //std::cout << entry.path().u8string() << std::endl;
    }
    for (int i = 0; i < entities.size(); i++)
    {
        std::cout << entities[i] << std::endl;
    }

}

void help(void)
{
    /*
    std::cout << "Usage:" << std::endl
        << " -p (prefix) - sets prefixes for folders like '(prefix)txt' or '(prefix)doc'" << std::endl
        << " -n - create folders named by just extensions" << std::endl
        << " -r - sorts unsorted files in existant folders using previous prefix" << std::endl
        << " -h - shows this message" << std::endl
        << " -c - unsort, bring files back from folders(also deleting folders)" << std::endl; */

    std::cout << "help message duh" << std::endl;
    return;
}

int main(int argc, char* argv[])
{
    std::cout << "Simple File Extension Sorter (rewritten)" << std::endl;
    if (argc > 1)
    {
        if (argv[1][1] == 'p' && argc == 3)
        {
            std::cout << "PLEAEEASE:3WORK ALREADY:3" << std::endl;
            sort(argv[2]);
        }
        else if (argv[1][1] == 'n')
        {
            sort(0);
        }
        else if (argv[1][1] == 'r')
        {
            std::ifstream cfg("cfg.sfes");
            if (cfg.good())
            {
                std::string prefix;
                std::getline(cfg, prefix);
                cfg.close();
                sort(prefix.data());
            }
            else
            {
                std::cout << "No previous sorts found! (No cfg.sfes file in the directory)";
            }

        }
        else if (argv[1][1] == 'c')
        {
            //not yet
            help();
        }
        else {
            help();
        }
    }    
    else {
        help();
    }
    return 1;
}
