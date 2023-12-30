#include<iostream>
#include <ctime>

using namespace std;

int check(long long int, int);
int check1(long long int, int);
int check2(long long int, int);
int check3(long long int, int);
int chec(long long int, int);




int main(){
    int in_int = 0;
    time_t start_time = time(0);
    while(1){
        if (check(in_int, 99) == 1835996258){
            cout << "The correct value is: " << in_int << endl;
            time_t stop_time = time(0);
            cout << "Total execution time: " << stop_time - start_time << endl;
            break;
        }
        else{
            cout<< "Try: " << in_int << endl;
            in_int += 1;
        }  
    }
}

int check(long long int input, int s) {
    return chec(input, s);
}

int check1(long long int input, int s) {
    long long int t = input;
    t += 4950;
    
    return chec(t, s);
}

int check2(long long int input, int s) {
    long long int t = input;
    if (s % 2 == 0) {
        t += 499500;
        return chec(t, s);
    }
    t -= 499500;
    return chec(t, s);
}

int check3(long long int input, int s) {
    long long int t = input;
    t += 49995000;
    return chec(t, s);
}

int chec(long long int input, int s){
    long long int result;
    if (s - 1 <= 0){
        result = input;
    } 
    else{
        if (2 * s % 3 == 0)
            result = check1(input, s - 1);
        if (2 * s % 3 == 1)
            result = check2(input, s - 1);
        if (2 * s % 3 == 2)
            result = check3(input, s - 1);
    }
    return result; 
}