import psycopg2  # pip install psycopg2-binary
import yaml # pip install PyYAML
import os

class ConnexionBD:

    def __init__(self):
        self.cnx = None
        self.params = None

    def getConnexion(self):
        try:
            print("- class connexionBD() is running ... \n\n")
            print("- config/Config.yml is loading ...")
            current_directory = os.path.dirname(os.path.abspath(__file__))
            print(current_directory)
            # Chemin relatif vers le fichier YAML
            yaml_file_path = os.path.join(current_directory, "../config/config.yaml")
            # get file and data
            if os.path.exists(yaml_file_path):
                with open(yaml_file_path, "r") as fic:
                    donnees = yaml.safe_load(fic)
                    config = donnees["postgreSQLAccess"]
                    db = config["database_name"]
                    host = config["host"]
                    port = config["port"]
                    usr = config["user"]["usr1"]
                    pwd = config["pwd"]["pwd1"]

                    self.cnx = psycopg2.connect(dbname=db,
                                  host=host,
                                  port=port,
                                  user=usr,
                                  password=pwd
                                  )
                    return self.cnx
            else:
                ("Le fichier YAML n'existe pas à l'emplacement spécifié.")
        except Exception as e:
            print(f"Erreur-CONNECTION ::: {e}")
        return self.cnx
