JAGS_FILES = $(wildcard *.jags)
HTML_FILES = $(patsubst %.jags,%.html,$(JAGS_FILES))

%.html : %.jags
	pygmentize -f html -O full -l jags -o $@ $<

all : $(HTML_FILES)

clean:
	-rm *.html
