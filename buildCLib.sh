gcc -g cSorts.c -o cSorts
# gcc -g -fPIC -Wall -Werror -Wextra -pedantic cSorts.c -shared -o cSorts.so 
gcc -fPIC -shared -o cSorts.so cSorts.c