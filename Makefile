##
## EPITECH PROJECT, 2021
## B-CNA-410-NAN-4-1-trade-arthur.adam
## File description:
## Makefile
##

NAME            =   307multigrains

RM              =   @rm -f

SOURCES         =   sources/

TESTS           =   tests/

COVERAGE        =   coverage

all: $(NAME)

$(NAME):
	@cp $(SOURCES)main.py $@
	@chmod +x $@

clean:
		$(RM) -r __pycache__
		$(RM) -r $(SOURCES)__pycache__

fclean: clean
		$(RM) $(NAME)

tests_run:
			$(COVERAGE) run --rcfile=.coveragerc -m --source=$(SOURCES) pytest --capture=sys -rA $(TESTS)
			$(COVERAGE) report -m

re: fclean all

.PHONY: all clean fclean re
