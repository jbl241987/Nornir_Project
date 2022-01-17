import csv
from nornir import InitNornir
from nornir_csv.plugins.inventory import CsvInventory
from nornir.core.plugins.inventory import InventoryPluginRegister
import nornir_csv

InventoryPluginRegister.register("CsvInventoryPlugin", CsvInventory)

nr = InitNornir(config_file='sample_config.yaml')

x = nr.inventory.hosts['R1'].password
print(x)


