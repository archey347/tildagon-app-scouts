install:
	-/root/.local/bin/mpremote a0 mkdir apps/scouts
	-/root/.local/bin/mpremote a0 mkdir apps/scouts/assets
	
	
update:
	/root/.local/bin/mpremote a0 cp ./app.py :/apps/scouts/
	/root/.local/bin/mpremote a0 cp ./metadata.json :/apps/scouts/
	/root/.local/bin/mpremote a0 cp ./assets/* :/apps/scouts/assets/

uninstall:
	-/root/.local/bin/mpremote a0 rm /apps/scouts/app.py
	-/root/.local/bin/mpremote a0 rm /apps/scouts/metadata.json
	-/root/.local/bin/mpremote a0 rm /apps/scouts/assets/se.jpg
	-/root/.local/bin/mpremote a0 rm /apps/scouts/assets/fleur.jpg
	-/root/.local/bin/mpremote a0 rm /apps/scouts/assets/cake.jpg

	-/root/.local/bin/mpremote a0 rmdir /apps/scouts/assets
	-/root/.local/bin/mpremote a0 rmdir /apps/scouts

shell:
	/root/.local/bin/mpremote a0

.PHONY: install shell