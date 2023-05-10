import os

from SettingsLoader.Concretes.CConfigurationLoader import CConfigurationLoader
from Configuration.Concretes.CGenericModuleConfiguration import CGenericModuleConfiguration
from Configuration.Concretes.CCustomModuleConfiguration import CCustomModuleConfiguration

WORKING_DIR = os.path.dirname(__file__)

if __name__ == "__main__": 
    configLoader = CConfigurationLoader(f"{WORKING_DIR}/../settings/", "settings.yml") 
    # configLoader.dumpObject(CGenericModuleConfiguration(moduleType="modulo_prova", outputDataFlows=["flusso1, flusso2"], inputDataFlows=[]))
    # configLoader.dumpObject(
    #     CCustomModuleConfiguration(moduleType="modulo_prova", outputDataFlows=["flusso1, flusso2"], inputDataFlows=[],
    #                                parametro_prova=3, prova_stringa="Ciaooo")
    #     )
    configLoader.loadConfiguration()
    configModule2 = configLoader.configuration.get("Modules").get("Modulo2")
    configModule3 = configLoader.configuration.get("Modules").get("Modulo3")
    configModule3.selectNeededParameters({"voluto_ma_non_presente": "valore_default"})
    configLoader.dumpObject(configModule3)