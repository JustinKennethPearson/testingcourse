### Little makefile to put the requirements document on the web.
SLIDESDIR=~/Harpo/public_html/Assets/Teaching
#List of the pdfs you want to create.
#Latex command to use
LATEX=pdflatex 
web: requirements_2020.pdf

requirements_2020.pdf: requirements_2020.tex
	$(LATEX) requirements_2020.tex
	$(LATEX) requirements_2020.tex
	cp requirements_2020.pdf $(SLIDESDIR)/requirements_2020.pdf

