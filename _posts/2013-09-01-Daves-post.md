---
title: Example for the Sept. 4th Class
layout: post
author: dpcolar
categories: post code
---

To add to the discussion for Wednesday's class, I wrote a few example lines of C and dumped the assembler code.
It is interesting to see where the compiler generated the same machine code for different instructions.

C code

```

#include <stdio.h>
main () {
	int number;	/* Declare an integer variable */
	number = 0;
	int one;
	one = 1;
	char c_one[2] = "01";
	char single[1] = "1";

	while (number < 10) {
		printf("%d \n", number);
	
		number++;
		number += 1;
		number = number + 1;
		number = number + one;
		number = atoi(c_one);
	}
}

```

Assember output via: <br>
	gcc -S -o example.s example.c <br>
	as -aljnd example.s > example.txt
	
```

	.file	"example.c"
	.section	.rodata
.LC0:
	.string	"%d \n"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	pushl	%ebp				The initial value for %ebp is usually 0. 
							  This is so debuggers know when to end following the link chain in a backtrace.
							  Think of %ebp as a reference point. 
							  For convenience, it is placed between the function arguments and local variables. 
							  That way, you access arguments with a positive offset, and variables with a negative offset.
	
	
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp				%esp - Stack Pointer
							 This register is implicitly manipulated by several CPU instructions 
							 (PUSH, POP, CALL, and RET among others), it always points to the last element 
							 used on the stack.

	.cfi_def_cfa_register 5
	andl	$-16, %esp
	subl	$32, %esp
	movl	$0, 24(%esp)			number = 0;
	movl	$1, 28(%esp)			one = 1;
	movw	$12592, 22(%esp)		move one word (2 bytes) containing the characters "01"
						  	"0" is 00110000 00000000 = 12288 (dec)
						  	"1" is 00000001 00110000 = 304 (dec)
	movb	$49, 21(%esp)			move one byte containing ASCII 49
	jmp	.L2				Jump the the marker .L2
.L3:
	movl	24(%esp), %eax	  		set up the parameters for printf 
	movl	%eax, 4(%esp)
	movl	$.LC0, (%esp)
	call	printf
	
						Note: compiler generates the same machine instructions
	addl	$1, 24(%esp)			number++;
	addl	$1, 24(%esp)			number += 1;
	addl	$1, 24(%esp)			number = number + 1;
	
	
	movl	28(%esp), %eax			move 'one'
	addl	%eax, 24(%esp)			add it to 'number'
	
	leal	22(%esp), %eax			Load effective address of 'c_one'
	movl	%eax, (%esp)			  change the stack pointer the the address of 'c_one'
	call	atoi				  convert a string to integer
							iterate through the characters of the string from left to right, 
							updating an accumulator with the growing integer value. Initially, the accumulator is set to 0. 
							At each character c, you multiply the accumulator by 10, and then add to it the value of the digit c
	movl	%eax, 24(%esp)			move the result back to 'number'
.L2:
						"while (number < 10) {"
		cmpl	$9, 24(%esp)		Compares two integers. It does this by subtracting the first operand from the second
		jle	.L3			jump to .L3 if number < or = 9
		leave				The compiler uses this instruction to free the used space by the function in the stack.
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 4.7.3-1ubuntu1) 4.7.3"
	.section	.note.GNU-stack,"",@progbits

```

References:<br>
	http://stackoverflow.com/questions/8361942/assembly-registers-esp-and-ebp
	http://download.intel.com/products/processor/manual/325462.pdf
	http://www.intel.com/content/www/us/en/processors/architectures-software-developer-manuals.html
