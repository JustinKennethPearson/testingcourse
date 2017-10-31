### Little makefile to put the requirements document on the web.
SLIDESDIR=~/Harpo/public_html/Teaching/Testing
#List of the pdfs you want to create.
#Latex command to use
LATEX=pdflatex 
web: requirements_2017.pdf

requirements_2017.pdf: requirements_2017.tex
	$(LATEX) requirements_2017.tex
	$(LATEX) requirements_2017.tex
	cp requirements_2017.pdf $(SLIDESDIR)/requirements_2017.pdf

