SRC = $(wildcard *.bug)
OBJ = $(patsubst %.bug,%.html,$(SRC))

%.html : %.bug
	pygmentize -f html -O full -l bugs -o $@ $<

all : $(OBJ)

clean:
	-rm *.html
