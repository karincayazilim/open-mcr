<!-- NOTE: This file is used to generate the manual.pdf, which must be
done as part of the build process (see /build_instructions.md) -->

![OpenMCR](wordmark.png)

# User Manual

## Basic Usage

### Installation

For download and installation instructions, see the project homepage:
https://github.com/iansan5653/open-mcr

### Printing Sheets

In order to use the OpenMCR software, students must use the provided multiple-
choice sheets. A printable PDF is available by clicking <kbd>Open Sheet</kbd> in the
software or by visiting the following link:
https://github.com/iansan5653/open-mcr/raw/master/code/assets/multiple_choice_sheet.pdf.

The program is robust and should work with most printers and scanners, however
best results will be obtained by using a laser printer in black & white mode
with the 'save toner' option turned off.

### Filling Sheets

Students should be instructed to fill bubbles throughly and erase completely
if necessary. It is not necessary to require any specific type of pen or pencil
to be used.

#### Creating Answer Keys

If you would like to take advantage of the automatic grading feature of the
software, you must provide it with one or more answer keys. To create an answer
key, simply print a normal sheet and put `ZZZZZZZZZZZZ` in the **Last Name**
field. Then, add a **Test Form Code** which will be used to match students' exams
with the correct answer key, and finally fill in the exam with the correct
answers.

This is optional - you can choose to just have the software read the exams and
not score them.

### Reading Sheets

Simply follow the following steps to process any number of filled exam sheets:

1. Scan all sheets using a standard scanner. Convert them into individual
   images and place them into a single folder. This includes answer keys - there
   is no need to scan them seperately.
2. Run the software. If you used the installer, a shortcut will be located in
   your Start menu. The sofware may take a moment to start.
3. Under **Select Input Folder**, click <kbd>Browse</kbd> and select the folder you
   stored the images in.
   - If you select the _convert multiple answers in a
     question to 'F'_ option, then if a student selects, for example, `A`
     _and_ `B` for a question, the output file will save that as `F` instead of
     `[A|B]`.
   - If you select the _save empty in questions as 'G'_ option, if a student
     skips a question by leaving it blank, the output file will save that as
     `G` instead of as a blank cell.
4. Under **Select Output Folder**, click <kbd>Browse</kbd> and select the folder where
   you would like to save the resulting CSV files.
   - If you select the _sort results by name_ option, results will be sorted
     by the students' last, first, and middle names (in that order). Otherwise,
     results will be saved in the order processed.
5. Click <kbd>Continue</kbd>.

### Output Files

After the program finishes processing, results will be saved as CSV files in
your selected output folder. These files can be opened in Excel or in any text
editor. Files will be saved with the time of processing to avoid overwriting any
existing files.

If you did not include any answer keys, one raw file will be saved with all of
the students' selected answers.

If you did include one or more answer keys, two more files will be saved in
addition to the aforementioned raw file. One of these files will have all of the
keys that were found, and the other will have the scored results. In the scored
file, questions are saved for each student as either `1` (correct) or `0`
(incorrect).

## Advanced Usage

### Providing a Premade Key File

If you do not want to create answer keys using the multiple choice form, or you
want to reuse answer keys across batches, you can select a CSV file under the
**Select Answer Keys File** heading. This file can be a key file previously
generated by OpenMCR, or it can be one you created yourself. If you create it
yourself, it should be in the following form:

```csv
Test Form Code, Q1, Q2, Q3, ...
             A,  A,  C,  B, ...
             B,  B,  B,  C, ...
             C,  E,  A,  D, ...
```

### Reordering Scored Results

If you want to be able to stastically analyze the exam results as a whole but also use
multiple keys, the easiest way to do so is to create a single exam and then
provide the other variations as randomly ordered versions of the original.
However, to be able to perform the analysis, you need
a way to reorder the results back to the original order.

To have this software automatically reorder the scored results, simply provide a
CSV file defining the order. Each row in this file represents a key, and each
column represents the position that that question should be moved to.

For example, if exam form `A` has questions 1, 2, and 3, exam form `B` might have
them in 3, 1, 2 order and `C` might have them in 3, 2, 1 order. This would result
in the following arrangement file:

```csv
Test Form Code, Q1, Q2, Q3
             A,  1,  2,  3
             B,  3,  1,  2
             C,  3,  2,  1
```

If this were the file you upload, then all of the exams with form `A` would be
left untouched while `B` and `C` would be rearranged to 1, 2, 3 order.
