install:
	-/root/.local/bin/mpremote a0 mkdir apps/scouts
	-/root/.local/bin/mpremote a0 mkdir apps/scouts/assets
	
	
update:
	/root/.local/bin/mpremote a0 cp ./src/app.py :/apps/scouts/
	/root/.local/bin/mpremote a0 cp ./src/metadata.json :/apps/scouts/
	/root/.local/bin/mpremote a0 cp ./src/assets/* :/apps/scouts/assets/
	

	


shell:
	/root/.local/bin/mpremote a0

.PHONY: install shell