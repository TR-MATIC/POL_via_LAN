# packages
import requests


# defs
class Climatix(object):
    def __init__(self, config_path="climatix_data.txt"):
        self.__config_path = config_path
        self.__config = {}
        # climatix_url / List of fields available/expected in TXT configuration.
        # climatix_name
        # climatix_pass
        # climatix_pin

    def load_config(self):
        config_file = open(self.__config_path, mode="r")
        config_data = config_file.readlines()
        config_file.close()
        for line in config_data:
            marker = line.find("=")
            key = line[0:marker]
            value = line[(marker + 1):].rstrip("\n")
            self.__config.update({key: value})
        return True

    def climatix_auth(self):
        climatix_auth = (self.__config["climatix_name"], self.__config["climatix_pass"])
        return climatix_auth

    def explore_view_node(self, oa_param, prefix):
        climatix_params = {"fn": "getviewnode"}
        climatix_params.update({"oa": oa_param})
        climatix_params.update({"pin": self.__config["climatix_pin"]})
        climatix_params.update({"lng": "eng"})
        get_view_node = requests.get(self.__config["climatix_url"], auth=self.climatix_auth(), params=climatix_params)
        view_node_data = get_view_node.json()
        new_oa_list = []
        print("{} --==##  {}  ##==--".format(prefix, view_node_data["values"][oa_param]["descr"]))
        for cnt, element in enumerate(view_node_data["values"][oa_param]["items"]):
            printout = []
            printout.append(element["descr"])
            if "oa" in element.keys():
                for key in element["oa"].keys():
                    printout.append("oa: " + key)
                    break
            if "link" in element.keys():
                printout.append("link: " + element["link"])
                if element["link"] not in ["NgAAAAAA", "NgASUgAA", "NgAwUgAA", "NgAxUgAA", "NgA6UgAA", "NgAcUgAA",
                                           "NgAJUgAA", "NgBEUgAA", "NgB2UgAA", "NgCAUgAA", "NgB3UgAA", "NgCKUgAA",
                                           "NgBsUgAA"]:
                    new_oa_list.append(element["link"])
            print("{} {} {}".format(prefix, cnt, printout))
        return new_oa_list
