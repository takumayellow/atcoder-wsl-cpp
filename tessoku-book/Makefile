LATEXMK := /Library/TeX/texbin/latexmk
MAIN_TEX := tex/main.tex
PDF := build/main.pdf

.PHONY: pdf clean distclean

pdf:
	$(LATEXMK) -r latexmkrc -lualatex $(MAIN_TEX)
	find build -maxdepth 1 -type f ! -name '*.pdf' -delete

clean:
	if [ -d build ]; then find build -maxdepth 1 -type f ! -name '*.pdf' -delete; fi

distclean: clean
	rm -f $(PDF)
