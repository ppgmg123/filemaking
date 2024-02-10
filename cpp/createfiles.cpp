// datastuff.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>
#include <stdlib.h>
using namespace std;

int main(int argc, char* argv[])
{
	string boolean;
	bool megabytes;
	// long bytes;
	int bytes;


	for (int i = 0; i < argc; ++i) {
		cout << argv[i] << "\n";
	}
	if (argc > 3 || argc < 3)
	{
		cout << "Use megabytes? : ";
		cin >> boolean;
		cout << "Enter your preferred bytes. : ";
		cin >> bytes;
		// bytes = strtol(&input2, &ptr, 10);
	}
	else
	{
		char* ptr;
		if (argv[2]){
			megabytes = true;
			bytes = strtol(argv[1], &ptr, 10);
		}
	}
	string confirm = "true";
	if (boolean == confirm) { megabytes = true; } else { megabytes = false; }
	std::ofstream ofs("ouput.txt", std::ios::binary | std::ios::out);
	if (!megabytes)
	{
		ofs.seekp((bytes)-1);
	}
	else
	{
		ofs.seekp((bytes * 1024 * 1024) - 1);
	}
	ofs.write("", 1);

	cout << "possible success";
	return 0;
}
