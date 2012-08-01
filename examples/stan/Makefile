STAN_FILES = $(wildcard *.stan)
HTML_FILES = $(patsubst %.stan,%.html,$(STAN_FILES))

%.html : %.stan
	pygmentize -f html -O full,style=emacs -l stan -o $@ $<

all : $(HTML_FILES)

clean:
	-rm *.html
