
all-y	+= crit

crit/crit: crit/crit-$(PYTHON)
	$(Q) PY_PKG_DIR=$(PY_PKG_DIR) sed -e 's,@py_pkg_dir@,$(PY_PKG_DIR),' $^ > $@
crit: crit/crit
.PHONY: crit

clean-crit:
	$(Q) $(RM) crit/crit
.PHONY: clean-crit
clean: clean-crit
mrproper: clean
