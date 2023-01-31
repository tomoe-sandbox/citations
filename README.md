# Assignment 0 - Citations

You will help to write a program that can parse a case citation, and return the case name and citation information.

Your program should: 
1. Ask for one input case citation with the following prompt:

``` Please input your complete case citation here, Quit to exit: ```

2. Accept as input a case citation. You do not need to validate the input or perform error trapping. You can assume that your users are obedient and will not deviate from the general format of a case citation. 

The general format is as follows:

``` Plaintiff v Defendant [Year] Vol CitatorName Page Number ```


3. Separate the case name from the citation and print the result, where the name and citation are separated by a comma:

    ``` Plaintiff v Defendant, [Year] Vol CitatorName Page ```

4. Save the case name and case citation into two separate lists. 

5. Have the program repeat steps 1 to 4, to prompt the user for input citations and process them until the user types "Quit". Your program's flow might look something like this:
> The ">" is used here to denote user input. It does not actually appear on your screen.
   
```
Please input your complete case citation here, Quit to exit:
> A v B [2011] 1 SLR 205
A v B, [2011] 1 SLR 205
Please input your complete case citation here, Quit to exit:
> Spandeck Engineering v DSTA [2007] 4 SLR(R) 100
Spandeck Engineering v DSTA, [2007] 4 SLR(R) 100
Please input your complete case citation here, Quit to exit:
> Donoghue v Stevenson [1932] AC 562
Donoghue v Stevenson, [1932] AC 562
```

6. On exiting the program, print out the lists of case names and case citations: 

``` Please input your complete case citation here, Quit to exit:
> Plaintiff v Defendant [Year] Vol CitatorName Page
Plaintiff v Defendant, [Year] Vol CitatorName Page
Please input your complete case citation here, Quit to exit:
> A v B [2011] 1 SLR 205
A v B, [2011] 1 SLR 205
Please input your complete case citation here, Quit to exit:
> Spandeck Engineering v DSTA [2007] 4 SLR(R) 100
Spandeck Engineering v DSTA, [2007] 4 SLR(R) 100
Please input your complete case citation here, Quit to exit:
> Donoghue v Stevenson [1932] AC 562
Donoghue v Stevenson, [1932] AC 562
Please input your complete case citation here, Quit to exit:
> Quit
['Plaintiff v Defendant', 'A v B', 'Spandeck Engineering v DSTA',
'Donoghue v Stevenson']
['[Year] Vol CitatorName Page', '[2011] 1 SLR 205', '[2007] 4 SLR(R)
100', '[1932] AC 562'] 
```