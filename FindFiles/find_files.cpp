#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <chrono>
#include <experimental/filesystem>

namespace fs = std::experimental::filesystem;

// Script to find all files in directory matching a search string

void find_nex_files(const fs::path &directory, const std::vector<std::string> &search_strings, std::map<std::string, std::vector<fs::path>> &nex_files) {
	for (const auto &entry : fs::recursive_directory_iterator(directory)) {
		if (fs::is_regular_file(entry) && entry.path().extension() == ".nex") {
			for (const auto &search_string : search_strings) {
				if (entry.path().filename().string().find(search_string) != std::string::npos) {
					nex_files[search_string].push_back(entry.path());
					break;
				}
			}
		}
	}
}

int main() {
	fs::path folder = "R:\\";
	std::vector<std::string> search_strings = { "SFN", "SCIN" }; 

	std::map<std::string, std::vector<fs::path>> nex_files;
	for (const auto &search_string : search_strings) {
		nex_files[search_string] = std::vector<fs::path>();
	}

	auto start_time = std::chrono::high_resolution_clock::now();
	find_nex_files(folder, search_strings, nex_files);
	auto end_time = std::chrono::high_resolution_clock::now();
	auto elapsed_time = std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time).count();

	std::cout << "\nFound .nex files:\n";
	for (const auto &search_string : search_strings) {
		std::cout << "Files with '" << search_string << "':\n";
		for (const auto &file : nex_files[search_string]) {
			std::cout << file << "\n";
		}
		std::cout << std::endl;
	}

	std::cout << "Time taken: " << elapsed_time << " ms" << std::endl;

	return 0;
}
