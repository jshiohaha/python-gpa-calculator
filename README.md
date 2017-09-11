# Python GPA Calculator

I got tired of doing *what-if* final class grades effect calculations on GPA by hand, so I created wrote some Python to do it for me. This accounts for accumulation of credits in high school, transfer credits, and general semesters. **BUT**, the magic comes when you're trying to *guestimate* what your GPA will be if you absolutely cannot pull your life together and end up with a few rough final course grades. Although, I have found this tool to be rather reassuring - usually a `B` vs. an `A` won't make *thaaat* big of a difference :-).

Admittedly, this isn't the best use of Python, but I wrote it a while back when I was first learning the language and wanted to use something without as much overhead as Java.

### How to use this
My system runs `python3` and everything works correctly without a virtual environment. All you have to do is clone the repo, update the `grades.txt` file with your specific semester info and run `python3 gpa.py`. The program will write to a file called `gpa.txt` regardless of whether it exists or not. If you have transfer credits or high school credits that affect your GPA, you can just add another section in the `grades.txt` input file (see below for format).

**Note**: You might have to change the `tables.py` file depending on your school's grading system. It currently uses the 7-point scale common at many U.S. universities where an `A` or `A+` is equivalent to a `4.0` GPA.

Here is a sample of the input file - `grades.txt`:
```
-2015F
0,P,Pass_NoPass
3,A,Too_Many_All_Nighters
3,B,Learned_ALot_But_ReallyHard
4,A+,Didnt_Even_Buy_The_Book
```
If you're still unsure how to format the `grades.txt` input file, look at the format when you clone the repo. You will find an example of what 2 semesters worth of classes look like as input as well as output in `gpa.txt`.

***

### TODO
- Incorporate some type of PDF parsing for transcripts to relieve need for csv input file... possibly using PyOCR?
- Make available online
