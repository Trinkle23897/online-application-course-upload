# ETHz/Chicago/Harvard courses auto upload

n+e

## Dependency

Python3, selenium, bs4

For installing selenium, you can refer to [here](https://morvanzhou.github.io/tutorials/data-manipulation/scraping/5-01-selenium/).

For installing Beautiful soup: `pip3 install bs4 --user`.

ps. I test the script in Chrome driver. If you use Firefox, please replace the `Chrome` in script.

## Usage

1. Replace your username and password in `ethz.py` or `chicago.py` or `harvard.py`;

2. Add your courses into `course.txt`. For Tsinghua students, it can directly copy the courses from English transcript page in [info](http://zhjw.cic.tsinghua.edu.cn/cj.cjCjbAll.do?m=bks_cjdcx&cjdlx=yw);

3. (Only for ETHz application) You should add the last 4 terms in `course.txt`;

   (Only for Harvard application) You should complete `math_courses` and `english_courses` in `harvard.py`;

4. `python3 ethz.py` or `python3 chicago.py` or `python3 harvard.py`;

5. Have a cup of tea.

## Format

The **full** format in `course.txt` is as follows (in a single line, separated by Tab):

- Course ID (12090043)
- Course Name (Military Theory and Skill Training)
- Credit (3)
- Grade (B+)
- Points (3.6)
- Semester (2016-Summer)
- hours Tutorial (0) (only for ETHz)
- hours Lectures (8) (only for ETHz)
- hours Practical Work (40) (only for ETHz)
- Weeks (3) (only for ETHz)

which results in: `12090043	Military Theory and Skill Training	3	B+	3.6	2016-Summer	0	8	40	3`

## What does it look like?

[Demo](http://ml.cs.tsinghua.edu.cn/~jiayi/video/IMG_7360.mov)