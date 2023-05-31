# Security Course Project

This repo is course work for a university course.
The idea is to code a web app with at least five security flaws.
This will be linked to from the course excercise answer essay,
where the flaws are pointed out and the ways to fix them are explained.

My chosen security flaws are:

- [Broken Access Control](secflaw_demo/questionnaire/views.py)
	- function from line 62
- [Injection](secflaw_demo/questionnaire/views.py)
	- function from line 21
- [Security Misconfiguration](secflaw_demo/.env)
	- additionally unneeded tool installations such as seen in requirements.txt are considered Security Misconfiguration 
- [CSRF -token](secflaw_demo/questionnaire/templates/questionnaire/question.html)
	- form on line 7
	- also [here](secflaw_demo/questionnaire/views.py) line 50
- [Vulnerable and Outdated Components](secflaw_demo/requirements.txt)
	- line 30
