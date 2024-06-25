install:
	/root/.local/bin/mpremote a0 mkdir apps/scouts
	/root/.local/bin/mpremote a0 cp -r ./src :/apps/scouts

update:
	/root/.local/bin/mpremote a0 cp ./src/* :/apps/scouts/


shell:
	/root/.local/bin/mpremote a0

.PHONY: install shell