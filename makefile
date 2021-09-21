### Little makefile to put the requirements document on the web.
#I cannot imagine that it is useful to anybody else except me.
#In the Lectures directory there is another makefile to copy
#the lectures accross to the web.
SLIDESDIR=~/Harpo/public_html/Assets/Teaching/Testing/
#List of the pdfs you want to create.
#Latex command to use
LATEX=pdflatex 
web: requirements_2021.pdf

requirements_2021.pdf: requirements_2021.tex
	$(LATEX) requirements_2021.tex
	$(LATEX) requirements_2021.tex
	cp requirements_2021.pdf $(SLIDESDIR)/requirements_2021.pdf

