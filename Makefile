install:
	-/root/.local/bin/mpremote a0 mkdir apps/scouts
	-/root/.local/bin/mpremote a0 mkdir apps/scouts/assets
	
	
update:
	/root/.local/bin/mpremote a0 cp ./app.py :/apps/scouts/
	/root/.local/bin/mpremote a0 cp ./metadata.json :/apps/scouts/
	/root/.local/bin/mpremote a0 cp ./assets/* :/apps/scouts/assets/

shell:
	/root/.local/bin/mpremote a0

.PHONY: install shell