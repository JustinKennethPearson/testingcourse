### Little makefile to put the requirements document on the web.
SLIDESDIR=~/Harpo/public_html/Teaching/Testing
#List of the pdfs you want to create.
#Latex command to use
LATEX=pdflatex 
web: requirements_2018.pdf

requirements_2018.pdf: requirements_2018.tex
	$(LATEX) requirements_2018.tex
	$(LATEX) requirements_2018.tex
	cp requirements_2018.pdf $(SLIDESDIR)/requirements_2018.pdf

