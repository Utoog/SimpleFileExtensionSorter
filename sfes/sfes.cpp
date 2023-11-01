#include <filesystem>
#include <iostream>
#include <string>

void sort(char* prefix)
{
    std::cout << "This doesn't work yet, prefix is '" << prefix << "'" << std::endl;
    std::string path = "./";

    for (const auto& entry : std::filesystem::directory_iterator(path))
    {
        std::cout << entry.path() << std::endl;
    }
}

int main(int argc, char** argv)
{
    std::cout << "Welcome to Simple File Extension Sorter v2.0" << std::endl;
    if (argc > 1) 
    {
        sort(argv[1]);
    }
    else {
        std::cout << "argument error" << std::endl;
        return -1;
    }
}
