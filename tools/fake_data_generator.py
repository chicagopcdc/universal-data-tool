import csv
import json

entityLabelsNumber = 10000
print("start entity labels creation - " + str(entityLabelsNumber))
entityLabels = []
for x in range(entityLabelsNumber):
  entityLabel = {}
  entityLabel["id"] = x
  entityLabel["displayName"] = "year_" + str(x)
  entityLabels.append(entityLabel)
print("end entity label creation")


print("start relationship labels creation")
relationLabels = [
      {
        "id": "criterion",
        "displayName": "Criterion"
      },
      {
        "id": "value",
        "displayName": "Value"
      },
      {
        "id": "operator",
        "displayName": "Operator"
      }
    ]
print("end relationship labels creation")


print("start sample creation")
tsvfile = open('/Users/lgraglia/Projects/PeDAL/repos/Clinical-Trial-Parser/data/input/clinical_trials.csv')
reader = csv.DictReader(tsvfile)
samples = []
for row in reader:
  sample = {}
  if "eligibility_criteria" in row and row["eligibility_criteria"]:
    sample["document"] = row["eligibility_criteria"]


  # sample["annotation"] = {}
  # entities = []
  # for :
	 # entity = {}
	 # entity["text"] = "Age"
	 # entity["textId"] = "id_" + 
	 # entity["label"] = get from entities labels above
	 # entity["start"] = 
	 # entity["end"] = 
	 # entities.append(entity)

  # sample["annotation"]["entities"] = entities
  samples.append(sample)
tsvfile.close()
print("end sample creation")


udt_config = {}
udt_config["name"] = "Test"
udt_config["interface"] = {}
udt_config["interface"]["type"] = "text_entity_relations"
udt_config["interface"]["description"] = ""
udt_config["interface"]["entityLabels"] = entityLabels
udt_config["interface"]["relationLabels"] = relationLabels
udt_config["samples"] = samples


out_file = open("./udt_config.json", "w")
json.dump(udt_config, out_file, indent = 6)
out_file.close()





