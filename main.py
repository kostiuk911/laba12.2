#include <forward_list>
#include <iostream>
using namespace std;

int main() {
    forward_list<int> numbers = { 4, 5, 1, 4, 2, 3, 4 };
    int input;
    cout << "Enter an element to remove the next occurrence: ";
    cin >> input;
    for (auto it = numbers.begin(); it != numbers.end(); ++it) {
        if (*it == input && next(it) != numbers.end()) {
            it = numbers.erase_after(it);
        }
    }
    cout << "Resulting list after removing next occurrence of " << input << ": ";
    for (auto number : numbers) {
        cout << number << " ";
    }
    cout << endl;
    return 0;
}
