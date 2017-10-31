# This is a personal makefile. It is to copy the lectures into my
# public html space.
#Run pdflatex twice to be sure
#I'm sure that this file will be of now use to anybody else.
#Destination of my slide directory.
SLIDESDIR=~/Harpo/public_html/Teaching/Testing/Slides
#List of the pdfs you want to create.
PDFS= lecture1.pdf  intro_to_course.pdf
#Latex command to use
LATEX=pdflatex 

all: $(PDFS)

%.pdf: %.tex
	$(LATEX) $<
	$(LATEX) $<
	cp $@ $(SLIDESDIR)/$@

#lecture1.pdf: lecture1.tex
#	$(LATEX) lecture1.tex
#	$(LATEX) lecture1.tex
#	cp lecture1.pdf $(SLIDESDIR)/lecture1.pdf
