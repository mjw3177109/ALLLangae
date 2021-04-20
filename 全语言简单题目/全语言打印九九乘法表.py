

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

