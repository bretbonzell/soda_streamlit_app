from datetime import datetime
import pandas as pd


def run_soda_scan(project_root, scan_name, checks_subpath = None):
    from soda.scan import Scan

    print("Running Soda Scan ...")
    config_file = f"{project_root}/configuration.yml"
    checks_path = f"{project_root}/checks.yml"

    if checks_subpath:
        checks_path += f"/{checks_subpath}"

    data_source = project_root

    scan = Scan()
    scan.set_verbose()
    scan.add_configuration_yaml_file(config_file)
    scan.set_data_source_name(data_source)
    scan.add_sodacl_yaml_files(checks_path)
    scan.set_scan_definition_name(scan_name)

    #scan_start = scan_results['scanStartTimestamp']

    result = scan.execute()

# this is the start of our scan objects
    scan_results = scan.get_scan_results()
    scan_start = scan_results['scanStartTimestamp']
    scan_date = scan_start[0:10]
    scan_date = datetime.strptime(scan_date, '%Y-%m-%d').date()
    match scan_results['hasFailures']:
        case True:
            full_result = 'Fail'
        case False:
            full_result = 'Pass'

    application = []
    name = []
    check_result = []
    value = []
    date = []
    dataset = []
    for i in scan_results['checks']:
        check_name = i['name']
        name.append(check_name)
        check_result_item = i['outcome']
        check_result.append(check_result_item)
        check_value = i['diagnostics']['value']
        value.append(check_value)
        check_dataset = i['table']
        dataset.append(check_dataset)
        date.append(scan_date)
        application.append(project_root)

    dict = {'application': application, 'name': name, 'result': check_result, 'value': value,
            'date': date, 'table': dataset}
    df = pd.DataFrame(dict)

    #add checks to df csv
    try:
        current_logs = pd.read_csv('soda_logs.csv')
        df = pd.concat([df, current_logs])
        df.to_csv('soda_logs.csv', index=False)
    except FileNotFoundError:
        df.to_csv('soda_logs.csv', index=False)

    return df
