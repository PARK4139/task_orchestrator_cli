def get_values_from_history_file(f_historical, pk_serial_filters=None):
    from sources.objects.pk_etc import PkFilter
    from sources.functions.get_list_calculated import get_list_calculated
    from sources.functions.get_historical_list import get_historical_list
    from sources.functions.is_url import is_url

    # TBD
    # paralel filter(priority) as another function

    values = []
    historical_lines = get_historical_list(f=f_historical)
    historical_lines = get_list_calculated(origin_list=historical_lines, dedup=True)

    for historical_line in historical_lines:
        if pk_serial_filters is None:
            values.append(historical_line)
        else:
            # serial filter
            if PkFilter.url_like in pk_serial_filters:
                if not is_url(historical_line):
                    continue
            # if PkFilter.url_like in pk_serial_filters:
            #     if not is_url(historical_line):
            #         continue
            values.append(historical_line)
    return values
