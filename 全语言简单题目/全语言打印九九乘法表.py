

"""
1 * 1 = 1

1 * 2 = 2 2 * 2 = 4

1 * 3 = 3 2 * 3 = 6 3 * 3 = 9

1 * 4 = 4 2 * 4 = 8 3 * 4 = 12 4 * 4 = 16

1 * 5 = 5 2 * 5 = 10 3 * 5 = 15 4 * 5 = 20 5 * 5 = 25

1 * 6 = 6 2 * 6 = 12 3 * 6 = 18 4 * 6 = 24 5 * 6 = 30 6 * 6 = 36

1 * 7 = 7 2 * 7 = 14 3 * 7 = 21 4 * 7 = 28 5 * 7 = 35 6 * 7 = 42 7 * 7 = 49

1 * 8 = 8 2 * 8 = 16 3 * 8 = 24 4 * 8 = 32 5 * 8 = 40 6 * 8 = 48 7 * 8 = 56 8 * 8 = 64

1 * 9 = 9 2 * 9 = 18 3 * 9 = 27 4 * 9 = 36 5 * 9 = 45 6 * 9 = 54 7 * 9 = 63 8 * 9 = 72 9 * 9 = 81


九九乘法表 :行和列 所有前面为1是第一列  2 是第二列
//*号后面的是行 1是第一行 二是第二行  由此可得出 要做两次循环  外层循环为行 里层循环为列


"""

"""
python

for i in range(1,10):
    for j in range(1,i+1):
        print("%s * %s = %s" %(j,i,j*i),end=" ")
    print("\r\n")
"""


"""
go

package main
import "fmt"

func main() {
	
	
	// 练习一下循环的使用
	for i := 1; i <= 9; i++ {
	    
	    for j:=1;j<=i;j++{
	       fmt.Printf("%d * %d= %d ", j,i,j*i);
	    }
	   fmt.Printf("\r\n");
		
	}
}
"""

"""
java
public class HelloWorld {
	public static void main(String[] args) {

		// 练习一下循环的使用
		for (int i=1; i<=9; i++) {
		    
		    for(int j =1; j<=i;j++){
		        System.out.printf("%d * %d =%d  ",j,i,j*i);
		    }
			System.out.printf("\r\n");
		}

	}
}
"""

"""
php
for($i=1;$i<=9;$i++){
	
	for($j=1;$j<=$i;$j++){
	    echo "{$j} * {$i}=".$j*$i;
	    echo "&nbsp;";
	}
	
	echo "<br/>";
}
"""

"""
javascript
for (let i=1; i<=9; i++) {
    var s = '';
    for(let j =1;j<=i;j++){
        	//console.log(`${j} *${i} =`,j*i);
        	s += j + '*' + i + '=' + (i * j) + '\t'
    }
    
   console.log(s);

}
"""



"""
C#
using System;

namespace bccn
{
	class Program
	{
		static void Main(string[] args)
		{
			
			
			// 练习一下循环的使用
			for (int i=1; i<=9; i++) {
			    for(int j=1;j<=i;j++){
			        	Console.Write("{0} * {1} ={2}  ", j,i,j*i);
			    }
				Console.Write("\r\n");
			}
			


		}
	}
}
"""

"""
C++
#include <stdio.h>
#include <iostream>
#include <math.h>
using namespace std;
int main() {
	int i;
	int j;
	for (i=1; i<=9; i++) {
	    for(j=1;j<=i;j++){
	        	cout << j <<"*"<<i<<"="<<j*i<<" ";
	    }
	cout <<endl;
	}	

	return 0;
}

"""

"""
C

#include <stdio.h>

int main() {

	
	// 练习一下循环的使用
	int i;
	int j;
	for (i=1; i<=9; i++) {
	    
	    for (j=1;j<=i;j++){
	        	printf(" %d * %d = %d ", j,i,(j*i));
	    }
	  	printf("\r\n");
	}
	


	
	return 0;
}
"""

