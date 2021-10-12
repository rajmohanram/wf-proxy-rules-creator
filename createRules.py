import yaml


# Create Wavefront pre-processor rules YAML file
def create_rules_yaml(metrics_obj, filename):
    with open(filename, 'w') as file:
        documents = yaml.dump(metrics_obj, file)


# Create a valid Rule name / ID
def get_rule_id(metric_name):
    rule_id = metric_name.replace('.*', '.any')
    rule_id = rule_id.replace('..', '.')
    rule_id = rule_id.replace('vmware.blockchain.', '').replace('.', '-')
    return rule_id


# Create object for rules file
def create_object_for_yaml(metrics):
    rules_object = dict()
    rules_list = list()
    for metric in metrics:
        rule_id = get_rule_id(metric)
        keys = ['rule', 'action', 'scope', 'match']
        values = [rule_id, 'allow', 'metricName', metric]
        rule_dict = dict(zip(keys, values))
        rules_list.append(rule_dict)
    rules_object['global'] = rules_list
    return rules_object


# Create metrics list
def get_metrics_list(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines


# Module entrypoint
if __name__ == "__main__":
    metrics_list_filename = 'metrics_list.txt'
    preprocessor_rules_filename = 'preprocessor_rules.yaml'
    metrics_list = get_metrics_list(metrics_list_filename)
    metrics_object = create_object_for_yaml(metrics_list)
    create_rules_yaml(metrics_object, preprocessor_rules_filename)
