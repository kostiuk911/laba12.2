#include "pch.h"
#include "CppUnitTest.h"
#include <forward_list>
using namespace std;

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest122
{
	TEST_CLASS(UnitTest122)
	{
	public:

		TEST_METHOD(TestRemoveNextOccurrence)
		{
			// Arrange
			forward_list<int> numbers = { 4, 5, 1, 4, 2, 3, 4 };
			int input = 4;
			int expected[] = { 4, 1, 4, 3, 4 };
			int index = 0;

			// Act
			for (auto it = numbers.begin(); it != numbers.end(); ++it) {
				if (*it == input && next(it) != numbers.end()) {
					it = numbers.erase_after(it);
				}
			}

			// Assert
			for (auto number : numbers) {
				Assert::AreEqual(expected[index], number);
				index++;
			}
		}

		TEST_METHOD(TestRemoveNextOccurrenceNotFound)
		{
			// Arrange
			forward_list<int> numbers = { 4, 5, 1, 4, 2, 3, 4 };
			int input = 6;
			int expected[] = { 4, 5, 1, 4, 2, 3, 4 };
			int index = 0;

			// Act
			for (auto it = numbers.begin(); it != numbers.end(); ++it) {
				if (*it == input && next(it) != numbers.end()) {
					it = numbers.erase_after(it);
				}
			}

			// Assert
			for (auto number : numbers) {
				Assert::AreEqual(expected[index], number);
				index++;
			}
		}
	};
}
